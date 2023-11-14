import json
from triangle import Triangle
from geopy import distance
from order import Order

def possible_route(order: Order) -> bool:
	# eventually this will be a db call to get a list of orders
	start = order.location_origin
	end = order.location_destination

	# perform this check on each route once we have a seeded DB
	route = json.load(open('order.json'))
	pickup = route['location_origin']
	dropoff = route['location_destination']

	valid_pickup = Triangle(
		start_final = distance.distance(start, end).mi,
		start_point = distance.distance(start, pickup).mi,
		final_point = distance.distance(end, pickup).mi).height < 2

	valid_dropoff = Triangle(
		start_final = distance.distance(start, end).mi,
		start_point = distance.distance(start, dropoff).mi,
		final_point = distance.distance(end, dropoff).mi).height < 2
	
	return valid_pickup and valid_dropoff
