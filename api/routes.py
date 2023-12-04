from typing import List

import googlemaps
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.schemas import OrderBase
from db.database import get_db
from db.models import Route, Location

router = APIRouter()


gmaps = googlemaps.Client(key='AIzaSyDzF5vH7j0uqDiydP7NhpSoq5CK1TneEDU')


def calculate_route_path(start_location: Location, end_location: Location) -> List[tuple]:
    directions_result = gmaps.directions(f"{start_location.latitude},{start_location.longitude}",
                                         f"{end_location.latitude},{end_location.longitude}",
                                         mode="driving")

    route_points = []
    for leg in directions_result[0]['legs']:
        for step in leg['steps']:
            route_points.append((step['start_location']['lat'], step['start_location']['lng']))

    return route_points


def check_distance_to_route(main_route_points: List[tuple], additional_point: tuple) -> bool:
    for point in main_route_points:
        distance = gmaps.distance_matrix(origins=[f"{point[0]},{point[1]}"],
                                         destinations=[f"{additional_point[0]},{additional_point[1]}"],
                                         mode='driving')
        if distance['rows'][0]['elements'][0]['distance']['value'] <= 1000:  # distance in meters
            return True
    return False


@router.post("/check_routes/")
def check_routes(order: OrderBase, db: Session = Depends(get_db)):
    additional_route_start = (order.location_origin_lat, order.location_origin_long)
    additional_route_end = (order.location_dest_lat, order.location_dest_long)
    possible_routes = []

    main_routes = db.query(Route).all()
    for route in main_routes:
        main_route_points = calculate_route_path(route.location_origin, route.location_dest)

        # Check if additional route can be added
        if check_distance_to_route(main_route_points, additional_route_start) or \
                check_distance_to_route(main_route_points, additional_route_end):
            possible_routes.append(route.id)

    return {"possible_routes": possible_routes}
