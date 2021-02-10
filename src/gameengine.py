import math
from commandership import CommanderShip
from homeplanet import HomePlanet

class GameEngine():
	def __init__(self):
		self.all_objects = []
		self.mobile_objects = []
		self.static_objects = []
		self.interactable_objects = []
		
		self.commandership = CommanderShip()
		self.all_objects.append(self.commandership)
		self.mobile_objects.append(self.commandership)
		self.homeplanet = HomePlanet(self.all_objects, self.interactable_objects)
		self.all_objects.append(self.homeplanet)
		self.static_objects.append(self.homeplanet)
		
	def get_objects(self):
		return self.all_objects
		
	def get_static_objects(self):
		return self.static_objects
		
	def get_interactable_objects(self):
		return self.interactable_objects
		
	def get_mobile_objects(self):
		return self.mobile_objects
		
	def calc_range_do_action(self):
		for object in self.interactable_objects:
			if self.in_closerange(self.commandership, object):
				self.commandership.set_object_in_closerange(object)
			else:
				self.commandership.set_object_in_closerange(0)
		
	def in_closerange(self, object1, object2):
		if math.dist(object1.get_pos(), object2.get_pos()) <= 30:
			return True
		else:
			return False
		
	def in_midrange(self, object1, object2):
		pass
		
	def in_longrange(self, object1, object2):
		pass
		
	def action(self):
		object = self.commandership.get_object_in_closerange()
		if object:
			object.interact()