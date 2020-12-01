import math

class GeneralSpaceObject():
	def __init__(self, dt):
		self.dt = dt
		self.x = 0
		self.y = 0
		self.ang = 0
		
	def get_x(self):
		return self.x
		
	def get_y(self):
		return self.y
		
	def get_angle(self):
		return self.ang