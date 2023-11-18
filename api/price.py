from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from business_logic.price_calculator import calculate
from db.database import get_db

router = APIRouter()


@router.get("/price")
def calculate_price(miles: int, pallets: int = 0, packages: int = 0, db: Session = Depends(get_db)) -> float:
    price = calculate(miles, pallets, packages)
    return price
