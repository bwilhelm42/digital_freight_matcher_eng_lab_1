from typing import Optional
import math

class Triangle(): 
	start_final: float
	start_point: float
	final_point: float
	area: float
	height: float

	def __init__(self, start_final, start_point, final_point):
		self.start_final = start_final
		self.start_point = start_point
		self.final_point = final_point
		self.area = self.__calculate_area()
		self.height = self.__calculate_height()
	
	def info(self):
		return f'start_final: {self.start_final}\nstart_point: {self.start_point}\nfinal_point: {self.final_point}\narea: {self.area}\nheight: {self.height}'

	def __calculate_area(self):
		semi = (self.start_final + self.start_point + self.final_point)/2
		return math.sqrt(semi * (semi - self.start_final) * (semi - self.start_point) * (semi - self.final_point))
	
	def __calculate_height(self):
		return 2 * (self.area / self.start_final)