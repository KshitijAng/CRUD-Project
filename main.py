from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
from enum import Enum
import uuid

class Status(str, Enum):
    PENDING = "Pending"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    FAILED = "Failed"

class Item(BaseModel):
    response_text: str | None = None
    status: Status = Status.PENDING
    source: str | None = "CHAT"
    tenant: str | None = "HIVERWEB"


app = FastAPI()

@app.get("/")
async def hello():
    return {"Hello World, this is a CRUD project for learning purposes."}

# 1. CREATE (POST)
db = []
@app.post("/items")
async def create_item(item: Item):

    now = datetime.now(timezone.utc)

    result = {
        "ug_id": str(uuid.uuid4()),
        "created_at": now,
        "updated_at": now,
        "response_text": item.response_text,
        "tenant": item.tenant,
        "status": item.status,
        "source": item.source,
    }

    db.append(result)
    return result

# 2. READ (GET)
@app.get("/items")
async def get_item():
    return db

# 2a. READ by ID (GET)
@app.get("/items/{ug_id}")
async def get_by_id(ug_id: str):
    for item in db:
        if item["ug_id"] == ug_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# UPDATE status of the item (PUT)
@app.put("/items/{ug_id}")
async def update_item(ug_id: str, status: Status):
    for item in db:
        if item["ug_id"] == ug_id:
            item["status"] = status
            item["updated_at"] = datetime.now(timezone.utc)
            return item
    
    raise HTTPException(status_code=404, detail="Item not found/Does not exist")


# DELETE (DELETE)
@app.delete("/items/{ug_id}")
async def remove_item(ug_id: str):
    for index, emp in enumerate(db):
        if emp["ug_id"] == ug_id:
            removed= db.pop(index)
            return {"message": "Item deleted", "item": removed}
    
    raise HTTPException(status_code=404, detail="Item not found")
