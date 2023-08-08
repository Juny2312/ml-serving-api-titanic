from typing import Union
import titanic 
from fastapi import FastAPI

app = FastAPI()


@app.get("/titanic")
def read_root():
    return {"Hello": "Here is for titanic model"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
