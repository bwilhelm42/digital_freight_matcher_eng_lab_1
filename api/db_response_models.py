from api.schemas import Order, Location
from pydantic import BaseModel


class OrderInfoResponse(BaseModel):
    order: Order
    start_location: Location
    end_location: Location
