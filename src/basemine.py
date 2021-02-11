from interactableobject import InteractableObject

class Basemine(InteractableObject):
	def __init__(self, max, exists, x, y):
		super().__init__(max, exists, x, y)
		self.name = "Basemine"
		self.costs = [0]