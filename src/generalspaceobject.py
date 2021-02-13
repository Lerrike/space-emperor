import math
from enumerations import *

class GeneralSpaceObject():
	def __init__(self):
		self.description = Description.Null
		self.x = 0
		self.y = 0
		self.angle = 0
		self.sprite = 0
		self.resources = 0
		self.created = 0
		self.exists = False
		
	def get_description(self):
		return self.description
		
	def get_created(self):
		return self.created
		
	def get_resources(self):
		return self.resources
		
	def get_pos(self):
		return [self.x, self.y]
		
	def set_pos(self, pos):
		self.x = pos[0]
		self.y = pos[1]
		
	def get_angle(self):
		return self.angle
		
	def get_sprite(self):
		return self.sprite
		
	def set_sprite(self, sprite):
		self.sprite = sprite
		
	def set_created(self, date):
		self.created = date
			
	def set_resources(self, amount):
		self.resources = amount
		
	def set_exist(self, value, object, engine):
		self.exists = value
		self.sprites[self.level].visible = value
		engine.add_to_all_objects(object)
		object.set_created([1,1,3300])