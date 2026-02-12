from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
from enum import Enum

class Item(BaseModel):
    response_text: str | None = None


app = FastAPI()

@app.get("/")
async def hello():
    return {"Hello World, this is a project"}

# CREATE (POST)
db = []
@app.post("/add_item/{ug_id}")
async def create_item(ug_id: int, item: Item, tenant: str | None = None):

    now = datetime.now(timezone.utc)

    result = {
        "ug_id": ug_id,
        "created_at": now,
        "updated_at": now,
        "response_text": item.response_text,
        "tenant": tenant
    }

    db.append(result)
    return result

# Read (GET)
@app.get("/get_items")
async def get_item():
    return db

# Update (PUT)
@app.put("/update_item/{ug_id}")
async def update_item(ug_id: int, response_text: str | None = None):
    for emp in db:
        if emp["ug_id"] == ug_id:
            if response_text is not None:
                emp["response_text"] = response_text
            
            emp["updated_at"] = datetime.utcnow()
            return emp
    
    raise HTTPException(status_code=404, detail="Item not found")


# Delete (DELETE)
@app.delete("/delete_item/{ug_id}")
async def remove_item(ug_id: int):
    for index, emp in enumerate(db):
        if emp["ug_id"] == ug_id:
            removed= db.pop(index)
            return {"message": "Item deleted", "item": removed}
    
    raise HTTPException(status_code=404, detail="Item not found")
    
