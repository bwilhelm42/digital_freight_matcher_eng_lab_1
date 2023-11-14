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

    def save_order(self):
        with open("order.json","a") as file:
            file.write(self.model_dump_json() + "\n")