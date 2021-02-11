from interactableobject import InteractableObject

class Basemine(InteractableObject):
	def __init__(self, created, max, exists, x, y):
		super().__init__(created, max, exists, x, y)
		self.name = "Basemine"
		self.interaction = "Take Almanite"
		self.costs = [0]
		
	def increment_resource(self):
		self.resources += 1
		
	def get_interaction_cost(self):
		return self.costs[self.level]
		
	def interact(self, cs):
		over = cs.add_resources(self.resources)
		self.set_resources(over)