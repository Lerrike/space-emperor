import math

class GeneralSpaceObject():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.ang = 0
		self.sprite = 0
		
	def get_x(self):
		return self.x
		
	def get_y(self):
		return self.y
		
	def get_angle(self):
		return self.ang
		
	def get_sprite(self):
		return self.sprite
		
	def set_sprite(self, sprite):
		self.sprite = sprite