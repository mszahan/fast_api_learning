from fastapi import APIRouter, Body, Request, status, HTTPException
from fastapi.responses import Response
from bson import ObjectId
from pymongo import ReturnDocument
from models import CarModel, CarCollection, UpdateCarModel, CarCollectionPagination


router = APIRouter()
CARS_PER_PAGE = 10


@router.post('/',
             response_description='Add new car',
             response_model=CarModel,
             status_code=status.HTTP_201_CREATED,
             response_model_by_alias=False,
             )
async def add_car(request: Request, car: CarModel = Body(...)):
    cars = request.app.db['cars']
    document = car.model_dump(by_alias=True, exclude=['id'])
    inserted = await cars.insert_one(document)
    return await cars.find_one({'_id': inserted.inserted_id})


@router.get('/',
            response_description='List all cars, paginated',
            response_model=CarCollectionPagination,
            response_model_by_alias=False,
            )
async def list_cars(request: Request, page: int = 1, limit: int = CARS_PER_PAGE):
    cars = request.app.db['cars']
    results = []
    cursor = cars.find().sort('brand').limit(limit).skip((page - 1) * limit)
    total_documents = await cars.count_documents({})
    has_more = total_documents > (page * limit)
    async for document in cursor:
        results.append(document)
    return CarCollectionPagination(
        cars=results,
        page=page,
        has_more=has_more,
    )

    # async for car in cars.find():
    #     results.append(car)
    # this line would be the replacement for 3 lines
    # return CarCollection( cars=await cars.find().to_list(1000) )
    # return CarCollection(cars=results)


@router.get('/{id}',
            response_description='Get a single car',
            response_model=CarModel,
            response_model_by_alias=False,
            )
async def show_car(id: str, request: Request):
    cars = request.app.db['cars']
    try:
        id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=404, detail='Invalid id')
    if (car := await cars.find_one({'_id': ObjectId(id)})) is not None:
        return car
    raise HTTPException(status_code=404, detail='Car not found')


@router.put('/{id}',
            response_description='Update a car',
            response_model=UpdateCarModel,
            response_model_by_alias=False,
            )
async def update_car(id: str, request: Request, car: UpdateCarModel = Body(...)):
    try:
        id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=404, detail='Invalid id')
    car = {k: v for k, v in car.model_dump(
        by_alias=True).items() if v is not None and k != '_id'}
    if len(car) >= 1:
        cars = request.app.db['cars']
        update_result = await cars.find_one_and_update(
            {'_id': ObjectId(id)}, {'$set': car},
            return_document=ReturnDocument.AFTER,

        )
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=404, detail='Car not found')

    if (existing_car := await cars.find_one({'_id': ObjectId(id)})) is not None:
        return existing_car
    raise HTTPException(status_code=404, detail='Car not found')


@router.delete('/{id}',
               response_description='Delete a car',
               )
async def delete_car(id: str, request: Request):
    try:
        id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=404, detail='Invalid id')
    cars = request.app.db['cars']
    delete_result = await cars.delete_one({'_id': ObjectId(id)})
    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail='Car not found')
