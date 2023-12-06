from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from business_logic.cost_calculator import calculate
from db.database import get_db

router = APIRouter()


@router.get("/cost")
def calculate_cost(miles: int, db: Session = Depends(get_db)) -> float:
    cost = calculate(miles)
    return cost