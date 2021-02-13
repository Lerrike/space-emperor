from interactableobject import InteractableObject
from enumerations import *

class Base(InteractableObject):
	def __init__(self, max, x, y, homeplanet):
		super().__init__(max, x, y)
		self.name = "Base"
		self.interaction = "Upgrade"
		self.homeplanet = homeplanet
		self.costs = [50,120,250,450,700,1000]
		
		
	def interact(self, engine):
		self.upgrade_level()
		self.sprites[self.level-1].visible = False
		self.sprites[self.level].visible = True
		self.homeplanet.level_action(engine)
		
	def get_interaction_cost(self):
		return self.costs[self.level]
		