from typing import List

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
    location_origin_id: int
    location_dest_id: int
    client_id: int
    cargo_id: int
    route_id: int
    contract_type: str


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
