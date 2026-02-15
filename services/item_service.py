"""
Service layer: business logic and DB access.
"""
import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from repositories.models.item_model import ItemModel
from dtos.item import ItemCreate, ItemUpdate


def create_item_service(db: Session, item_schema: ItemCreate) -> ItemModel:
    now = datetime.utcnow()
    db_item = ItemModel(
        ug_id=str(uuid.uuid4()),
        response_text=item_schema.response_text,
        status=item_schema.status.value,
        source=item_schema.source.value,
        tenant=item_schema.tenant.value,
        created_at=now,
        updated_at=now,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def list_items_service(db: Session) -> list[ItemModel]:
    return db.query(ItemModel).all()


def get_item_service(db: Session, ug_id: str) -> ItemModel | None:
    return db.query(ItemModel).filter(ItemModel.ug_id == ug_id).first()


def update_item_service(db: Session, ug_id: str, item_schema: ItemUpdate) -> ItemModel | None:
    db_item = get_item_service(db, ug_id)
    if db_item is None:
        return None
    db_item.status = item_schema.status.value
    db_item.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item_service(db: Session, ug_id: str) -> bool:
    db_item = get_item_service(db, ug_id)
    if db_item is None:
        return False
    db.delete(db_item)
    db.commit()
    return True
