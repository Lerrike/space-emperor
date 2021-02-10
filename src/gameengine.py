import math
from commandership import CommanderShip
from homeplanet import HomePlanet

class GameEngine():
	def __init__(self):
		self.all_objects = []
		self.mobile_objects = []
		self.static_objects = []
		self.secondary_static_objects = []
		
		self.commandership = CommanderShip()
		self.all_objects.append(self.commandership)
		self.mobile_objects.append(self.commandership)
		self.homeplanet = HomePlanet()
		self.all_objects.append(self.homeplanet)
		self.static_objects.append(self.homeplanet)
		
	def get_objects(self):
		return self.all_objects
		
	def get_static_objects(self):
		return self.static_objects
		
	def get_secondary_static_objects(self):
		return self.secondary_static_objects
		
	def get_mobile_objects(self):
		return self.mobile_objects
		
	def in_action_range(self, object):
		if math.dist(self.commandership.get_pos(), object.get_pos()) <= 60:
			return True
		else
			return False
		
	def in_view_range(self, object1, object2):
		pass
		
	def in_map_range(self, object1, object2):
		pass
		
	def action(self):
		for object in self.get_static_objects():
			if self.in_action_range(object):
				pass