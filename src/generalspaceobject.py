import math

class GeneralSpaceObject():
	def __init__(self, created):
		self.x = 0
		self.y = 0
		self.ang = 0
		self.sprite = 0
		self.storage = 0
		self.created = created
		
	def get_created(self):
		return self.created
		
	def get_storage(self):
		return self.storage
		
	def get_pos(self):
		return [self.x, self.y]
		
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
		
	def set_created(self, date):
		self.created = date