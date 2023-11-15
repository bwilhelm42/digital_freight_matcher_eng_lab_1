from typing import Union
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from order import Order
from route_evaluator import possible_route
from price_calculator import calculate

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
    return calculate(miles, pallets, packages)

@app.post("/get_routes")
def get_routes(order: Order) -> bool:
    return possible_route(order)
    