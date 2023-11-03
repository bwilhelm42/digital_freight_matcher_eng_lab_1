from typing import Union
from fastapi import FastAPI, Request

# this is to validate and parse json payloads
from pydantic import BaseModel

class Order(BaseModel):
    location_origin: float
    location_destination: float
    client: str
    cargo: str
    contract_type: str

def save_order(order_object: Order):
    with open("file.json","a") as file:
        file.write(order_object.model_dump_json() + "\n")