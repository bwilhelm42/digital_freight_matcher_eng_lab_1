from typing import Union, Tuple
from fastapi import FastAPI, Request

# this is to validate and parse json payloads
from pydantic import BaseModel

class Order(BaseModel):
    location_origin: Tuple[float, float]
    location_destination: Tuple[float, float]
    client: str
    cargo: str
    contract_type: str

def save_order(order_object: Order):
    with open("file.json","a") as file:
        file.write(order_object.model_dump_json() + "\n")