"""
Router: route definitions and get_db. Delegates to controller.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repositories.Orm import SessionLocal
from dtos.item import ItemCreate, ItemUpdate, ItemResponse
from controllers import item_controller

router = APIRouter(prefix="/items", tags=["Items"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return item_controller.create_item(item, db)


@router.get("/", response_model=list[ItemResponse])
def list_items(db: Session = Depends(get_db)):
    return item_controller.list_items(db)


@router.get("/{ug_id}", response_model=ItemResponse)
def get_item(ug_id: str, db: Session = Depends(get_db)):
    return item_controller.get_item(ug_id, db)


@router.patch("/{ug_id}", response_model=ItemResponse)
def update_item(ug_id: str, item: ItemUpdate, db: Session = Depends(get_db)):
    return item_controller.update_item(ug_id, item, db)


@router.delete("/{ug_id}", status_code=204)
def delete_item(ug_id: str, db: Session = Depends(get_db)):
    item_controller.delete_item(ug_id, db)
