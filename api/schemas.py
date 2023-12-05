from typing import List, Optional

from pydantic import BaseModel


class LocationBase(BaseModel):
    latitude: float
    longitude: float
    marked: bool


class Location(LocationBase):
    id: int
    client_id: int

    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    name: str


class Client(ClientBase):
    id: int
    locations: List[Location] = []

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    location_origin_lat: float
    location_origin_long: float
    location_dest_lat: float
    location_dest_long: float
    client_id: Optional[int]
    cargo_id: Optional[int]
    route_id: Optional[int]
    contract_type: Optional[str]


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True


class PackageBase(BaseModel):
    volume: float
    weight: float
    type: str
    cargo_id: int


class Package(PackageBase):
    id: int

    class Config:
        orm_mode = True


class CargoBase(BaseModel):
    volume: float
    weight: float
    type: str


class Cargo(CargoBase):
    id: int
    orders: List[Order] = []
    packages: List[Package] = []

    class Config:
        orm_mode = True


class TruckBase(BaseModel):
    autonomy: float
    capacity: float
    type: str


class Truck(TruckBase):
    id: int
    cargos: List[Cargo] = []

    class Config:
        orm_mode = True


class RouteBase(BaseModel):
    location_origin_id: int
    location_dest_id: int
    profitability: float


class Route(RouteBase):
    id: int
    orders: List[Order] = []
    path: List[Location] = []

    class Config:
        orm_mode = True
