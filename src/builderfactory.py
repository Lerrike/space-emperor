from interactableobject import InteractableObject

class BuilderFactory(InteractableObject):
	def __init__(self, max, exists, x, y):
		super().__init__(max, exists, x, y)
		self.name = "Builder Factory"
		self.interaction = "Make a Engineering Unit"
		self.costs = [25]
		self.angle = 90