from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    is_offer:bool = None

@app.put("/{item_id}")
async def update_item(item_id:int,item:Item):
    return {
        "item_name":item.name,
        "item_id":item_id
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)