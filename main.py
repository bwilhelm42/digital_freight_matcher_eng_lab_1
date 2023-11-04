from typing import Union
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

import order

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

@app.get("/price")
def calculate_price(miles: int,
                    pallets: int = 0,
                    packages: int = 0):
    markup = 0.5
    pallet_cost_per_mile = 0.0683053788345865
    package_cost_per_mile = 0.0192470664936441
    pallet_cost = pallets * pallet_cost_per_mile * miles
    package_cost = packages * package_cost_per_mile * miles
    return (package_cost + pallet_cost) * (1 + markup)