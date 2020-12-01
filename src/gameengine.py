from commandership import CommanderShip
from homeplanet import HomePlanet

class GameEngine():
	def __init__(self):
		self.dt = 1.0/30.0
		self.commandership = CommanderShip(self.dt)
		self.homeplanet = HomePlanet(self.dt)