import math

class Triangle(): 
	start_to_final: float
	start_to_point: float
	final_to_point: float
	area: float
	height: float

	def __init__(self, start_to_final: float, start_to_point: float, final_to_point: float):
		self.start_to_final = start_to_final
		self.start_to_point = start_to_point
		self.final_to_point = final_to_point
		self.area = self.__calculate_area()
		self.height = self.__calculate_height()
	
	def info(self) -> str:
		return (f'start_to_final: {self.start_to_final}\n'
			f'start_to_point: {self.start_to_point}\n'
			f'final_to_point: {self.final_to_point}\n'
			f'area: {self.area}\nheight: {self.height}')

	def __calculate_area(self) -> float:
		semi = (self.start_to_final + self.start_to_point + self.final_to_point)/2
		return math.sqrt(semi * (semi - self.start_to_final) * (semi - self.start_to_point) * (semi - self.final_to_point))
	
	def __calculate_height(self) -> float:
		return 2 * (self.area / self.start_to_final)