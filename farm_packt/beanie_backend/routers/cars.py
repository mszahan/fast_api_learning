from typing import list
import cloudinary
from beanie import PydanticObjectId, WriteRules
from cloudinary import uploader  # noqa: F401
from fastapi import APIRouter, Depends, HTTPException, status, File, Form, UploadFile
from authentication import AuthHandler
from config import BaseConfig
from models import Car, UpdateCar, User


auth_handler = AuthHandler()


settings = BaseConfig()

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_SECRET_KEY,
)


router = APIRouter()


@router.get('/', response_model=list[Car])
async def get_cars():
    cars = await Car.find_all().to_list()
    return cars


@router.get('/{car_id}', response_model=Car)
async def get_car(car_id: PydanticObjectId):
    car = await Car.get(car_id)
    if not car:
        raise HTTPException(
            satatus_code=status.HTTP_404_NOT_FOUND, detail="Car not found")
    return car


@router.post('/', response_description='Add new car with picture',
             response_model=Car,
             status_code=status.HTTP_201_CREATED)
async def add_car_with_pictue(
    brand: str = Form('brand'),
    make: str = Form('make'),
    year: int = Form('year'),
    cm3: int = Form('cm3'),
    km: int = Form('km'),
    price: int = Form('price'),
    picture: UploadFile = File('picture'),
    user_data=Depends(auth_handler.auth_wrapper),
):
    cloudinary_image = cloudinary.uploader.upload(
        picture.file,
        folder='FARM2',
        crop='fill',
        width=800,
        gravity='auto',
    )
    picture_url = cloudinary_image.get('secure_url')
    user = await User.get(user_data['user_id'])
    car = Car(
        brand=brand,
        make=make,
        year=year,
        cm3=cm3,
        km=km,
        price=price,
        picture=picture_url,
        user=user,
    )
    return await car.insert(link_rule=WriteRules.WRITE)


@router.put('/{car_id}', response_model=Car)
async def update_car(
    car_id: PydanticObjectId,
    cardata: UpdateCar
):
    car = await Car.get(car_id)
    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Car not found")
    updated_car = {k: v for k, v in cardata.model_dump().items()
                   if v is not None}
    return await car.set(updated_car)


@router.delete('/{car_id}')
async def delete_car(car_id: PydanticObjectId):
    car = await Car.get(car_id)
    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Car not found")
    await car.delete()
    return {"message": "Car deleted successfully"}
