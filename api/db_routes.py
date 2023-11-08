from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import api.schemas as schemas
import db.models as models
from db.database import get_db

router = APIRouter()


# Clients
@router.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientBase, db: Session = Depends(get_db)):
    db_client = models.Client(**client.model_dump())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


@router.get("/clients/", response_model=List[schemas.Client])
def get_clients(db: Session = Depends(get_db)):
    clients = db.query(models.Client).all()
    return clients


# Locations
@router.post("/locations/", response_model=schemas.Location)
def create_location(location: schemas.LocationBase, db: Session = Depends(get_db)):
    db_location = models.Location(**location.model_dump())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location


@router.get("/locations/", response_model=List[schemas.Location])
def get_locations(db: Session = Depends(get_db)):
    locations = db.query(models.Location).all()
    return locations


# Orders
@router.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderBase, db: Session = Depends(get_db)):
    db_order = models.Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@router.get("/orders/", response_model=List[schemas.Order])
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(models.Order).all()
    return orders


# Cargo
@router.post("/cargo/", response_model=schemas.Cargo)
def create_cargo(cargo: schemas.CargoBase, db: Session = Depends(get_db)):
    db_cargo = models.Cargo(**cargo.model_dump())
    db.add(db_cargo)
    db.commit()
    db.refresh(db_cargo)
    return db_cargo


@router.get("/cargo/", response_model=List[schemas.Cargo])
def get_cargo(db: Session = Depends(get_db)):
    cargo = db.query(models.Cargo).all()
    return cargo


# Packages
@router.post("/packages/", response_model=schemas.Package)
def create_package(package: schemas.PackageBase, db: Session = Depends(get_db)):
    db_package = models.Package(**package.model_dump())
    db.add(db_package)
    db.commit()
    db.refresh(db_package)
    return db_package


@router.get("/packages/", response_model=List[schemas.Package])
def get_packages(db: Session = Depends(get_db)):
    packages = db.query(models.Package).all()
    return packages


# Trucks
@router.post("/trucks/", response_model=schemas.Truck)
def create_truck(truck: schemas.TruckBase, db: Session = Depends(get_db)):
    db_truck = models.Truck(**truck.model_dump())
    db.add(db_truck)
    db.commit()
    db.refresh(db_truck)
    return db_truck


@router.get("/trucks/", response_model=List[schemas.Truck])
def get_trucks(db: Session = Depends(get_db)):
    trucks = db.query(models.Truck).all()
    return trucks


# Routes
@router.post("/routes/", response_model=schemas.Route)
def create_route(route: schemas.RouteBase, db: Session = Depends(get_db)):
    db_route = models.Route(**route.model_dump())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route


@router.get("/routes/", response_model=List[schemas.Route])
def get_routes(db: Session = Depends(get_db)):
    routes = db.query(models.Route).all()
    return routes
