from interactableobject import InteractableObject

class Basemine(InteractableObject):
	def __init__(self, created, max, exists, x, y):
		super().__init__(created, max, exists, x, y)
		self.name = "Basemine"
		self.interaction = "Take Almanite"
		self.costs = [0]
		self.storage = 0
		
	def increment_resource(self):
		self.storage += 1
		
	def get_interaction_cost(self):
		return self.costs[self.level]