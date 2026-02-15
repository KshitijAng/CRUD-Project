from datetime import datetime
from pydantic import BaseModel
from utils.enums import StatusEnum, SourceEnum, TenantEnum


class ItemCreate(BaseModel):
    response_text: str | None = None
    status: StatusEnum
    source: SourceEnum
    tenant: TenantEnum


class ItemUpdate(BaseModel):
    status: StatusEnum


class ItemResponse(BaseModel):
    ug_id: str
    response_text: str | None
    status: str
    source: str
    tenant: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
