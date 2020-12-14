from commandership import CommanderShip
from homeplanet import HomePlanet

class GameEngine():
	def __init__(self):
		self.dt = 1.0/30.0
		
		self.objects = []
		self.mobile_objects = []
		self.static_objects = []
		self.secondary_static_objects = []
		
		self.commandership = CommanderShip(self.dt)
		self.objects.append(self.commandership)
		self.mobile_objects.append(self.commandership)
		self.homeplanet = HomePlanet(self.dt)
		self.objects.append(self.homeplanet)
		self.static_objects.append(self.homeplanet)
		
	def get_objects(self):
		return self.objects
		
	def get_static_objects(self):
		return self.static_objects
		
	def get_secondary_static_objects(self):
		return self.secondary_static_objects
		
	def get_mobile_objects(self):
		return self.mobile_objects
		