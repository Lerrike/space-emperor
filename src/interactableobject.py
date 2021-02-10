from generalspaceobject import GeneralSpaceObject

class InteractableObject(GeneralSpaceObject):
	def __init__(self):
		super().__init__()
		self.load = 0
		
	def load_interaction(self):
		if self.load >= 100:
			self.interact()
			self.load = 0
		self.load += 1
			
	def get_load(self):
		return self.load
		
	def reset_load(self):
		self.load = 0
		
	def interact(self):
		pass