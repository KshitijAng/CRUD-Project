from sqlalchemy import Column, String, DateTime, func
from ..Orm import ORMBase

class ItemModel(ORMBase):
    
    __tablename__ = "items"

    ug_id = Column(String, primary_key=True, index=True)
    response_text = Column(String, nullable=True)
    status = Column(String)
    source = Column(String)
    tenant = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now())
