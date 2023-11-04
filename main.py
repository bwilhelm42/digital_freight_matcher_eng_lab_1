import json
from typing import Union
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

import order
import triangle

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "muhhhtttafuckaaasss"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/orders", response_class=PlainTextResponse)
def get_order(order_details: order.Order):
    order.save_order(order_details)
    return f"order saved\n"

@app.get("/validate_order")
def validate_point(lat: int, lon: int):
    j = json.loads('file.json')
    o = order.Order(j)
    return lat + lon
    