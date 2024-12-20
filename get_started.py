from fastapi import FastAPI, HTTPException
from test import items
from pydantic import BaseModel
app = FastAPI()


#this asks for json format in curl, so values are text only
class Item(BaseModel):
    text: str = None
    is_done: bool = False

#define a route path for http get method; when client visits this path root function is called
@app.get("/")
def root():
    return {"Hello": "World"}

#
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    print(items)
    return items

@app.get("/items",response_model=list[Item])
def list_items(limit: int=10):
    return items[0:limit]




@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail='Item not found')