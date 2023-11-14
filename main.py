import json
from typing import Union
from typing import Tuple
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

import route_evaluator
from order import Order
import price_calculator

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "everyone"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/orders", response_class=PlainTextResponse)
def get_order(order: Order):
    order.save_order()
    return f"order saved\n"

@app.get("/price")
def calculate_price(miles: int, pallets: int = 0, packages: int = 0) -> float:
    return price_calculator.calculate(miles, pallets, packages)

@app.post("/validate_order")
def get_routes(order: Order) -> bool:
    return route_evaluator.possible_route(order)
    