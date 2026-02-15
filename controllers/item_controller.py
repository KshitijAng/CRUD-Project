"""
Controller: same commands as before (create, list, get, update, delete).
Handles HTTP (e.g. 404) and calls service.
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session
from dtos.item import ItemCreate, ItemUpdate, ItemResponse
from services import item_service


def create_item(item: ItemCreate, db: Session) -> ItemResponse:
    return item_service.create_item_service(db, item)


def list_items(db: Session) -> list[ItemResponse]:
    return item_service.list_items_service(db)


def get_item(ug_id: str, db: Session) -> ItemResponse:
    result = item_service.get_item_service(db, ug_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return result


def update_item(ug_id: str, item: ItemUpdate, db: Session) -> ItemResponse:
    updated = item_service.update_item_service(db, ug_id, item)
    if updated is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


def delete_item(ug_id: str, db: Session) -> None:
    if not item_service.delete_item_service(db, ug_id):
        raise HTTPException(status_code=404, detail="Item not found")
