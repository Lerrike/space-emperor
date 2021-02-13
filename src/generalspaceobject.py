import math
from enumerations import *

class GeneralSpaceObject():
	def __init__(self):
		self.description = EngineList.Null
		self.x = 0
		self.y = 0
		self.angle = 0
		self.sprites = 0
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
		
	def set_exist(self, value, engine):
		self.exists = value
		if self.sprites:
			self.sprites[self.level].visible = value
		elif self.sprite:
			self.sprite.visible = value
		self.set_created(engine.get_date())
		
		engine.add_all_objects(self)
		type = self.get_description()
		if type == EngineList.Static:
			engine.add_static(self)
		elif type == EngineList.Interactable:
			engine.add_interactable(self)
		elif type == EngineList.AI:
			engine.add_ai(self)