from fastapi import Depends
from sqlalchemy.orm import Session

from typing import Optional

import api.db_routes as db_routes
from db.database import get_db
from db.models import Order
from db.models import Route
from db.models import Location
from triangle import Triangle
from geopy import distance

def get_possible_route(order: Order, db: Session = Depends(get_db)) -> Optional[Route]:
	pickup = order.location_origin
	dropoff = order.location_dest

	routes = db_routes.get_routes(db)

	for route in routes:
		if (valid_point(pickup, route) and valid_point(dropoff, route)):
			return route

	return None

def valid_point(point: Location, route: Route):
	return Triangle(
		start_to_final = distance.distance(route.location_origin, route.location_dest).mi,
		start_to_point = distance.distance(route.location_origin, point).mi,
		final_to_point = distance.distance(route.location_dest, point).mi).height < 2