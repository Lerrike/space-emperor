from commandership import CommanderShip

class GameEngine():
	def __init__(self):
		self.dt = 1.0/30.0
		self.commandership = CommanderShip(self.dt)