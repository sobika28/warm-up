
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Day 3 Practice API")


# GET endpoint to check whether the API is running
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# GET endpoint to retrieve an item by ID
@app.get("/items/{id}")
def get_item(id: int):
    return {"item_id": id, "name": f"Item {id}"}


# Pydantic model for validating incoming item data
class Item(BaseModel):
    name: str
    price: float


# POST endpoint to create an item
@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "item": item
    }
