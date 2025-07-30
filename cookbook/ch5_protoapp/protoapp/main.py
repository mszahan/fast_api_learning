from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from protoapp.database import SessionLocal, Item


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ItemSchema(BaseModel):
    name: str
    color: str


app = FastAPI()


@app.get('/home')
async def read_main():
    return {'message': 'Hello World'}


@app.post('/item/', response_model=int, status_code=status.HTTP_201_CREATED)
async def add_item(item: ItemSchema, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, color=item.color)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item.id


@app.get('/item/{item_id}', response_model=ItemSchema)
async def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return item
