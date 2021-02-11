from interactableobject import InteractableObject

class Base(InteractableObject):
	def __init__(self, created, max, exists, x, y, homeplanet):
		super().__init__(created, max, exists, x, y)
		self.name = "Base"
		self.interaction = "Upgrade"
		self.homeplanet = homeplanet
		self.costs = [50,120,250,450,700,1000]
		
		
	def interact(self):
		self.upgrade_level()
		self.sprites[self.level-1].visible = False
		self.sprites[self.level].visible = True
		self.homeplanet.level_action()
		
	def get_interaction_cost(self):
		return self.costs[self.level]
		