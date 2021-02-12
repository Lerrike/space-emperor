from interactableobject import InteractableObject

class Basemine(InteractableObject):
	def __init__(self, max, exists, x, y):
		super().__init__(max, exists, x, y)
		self.name = "Basemine"
		self.interaction = "Take Almanite"
		self.costs = [0]
		
	def increment_resource(self):
		self.resources += 1
		
	def interact(self, cs):
		over = cs.add_resources(self.resources)
		self.set_resources(over)