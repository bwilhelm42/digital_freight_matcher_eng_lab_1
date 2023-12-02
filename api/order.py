from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import Order
from db.models import Route
from typing import Optional
from business_logic.route_evaluator import get_possible_route
from api.price import calculate_price
from geopy import distance

router = APIRouter()

@router.post("/submit_order")
def submit_order(order: Order, db: Session = Depends(get_db)) -> Optional[float]:
	route = get_possible_route(order)
	if not route:
		return None
	order_distance = distance.distance(order.location_origin, order.location_dest).mi
	price = calculate_price(order_distance, packages = len(order.cargo.packages))
	return price