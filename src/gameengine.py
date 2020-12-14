from commandership import CommanderShip
from homeplanet import HomePlanet

class GameEngine():
	def __init__(self):
		self.dt = 1.0/30.0
		
		self.objects = []
		self.commandership = CommanderShip(self.dt)
		self.add_object(self.commandership)
		self.homeplanet = HomePlanet(self.dt)
		self.add_object(self.homeplanet)
		
	def get_objects(self):
		return self.objects
		
	def add_object(self, object):
		self.objects.append(object)