from interactableobject import InteractableObject

class Basemine(InteractableObject):
	def __init__(self, max, x, y):
		super().__init__(max, x, y)
		self.name = "Basemine"
		self.interaction = "Take Almanite"
		self.costs = [0]
		
	def increment_resource(self):
		self.resources += 1
		
	def interact(self, engine):
		over = engine.get_cs().add_resources(self.resources)
		self.set_resources(over)