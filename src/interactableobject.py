from generalspaceobject import GeneralSpaceObject

class InteractableObject(GeneralSpaceObject):
	def __init__(self):
		super().__init__()
		self.load = 0
		self.level = 0
		
	def load_interaction(self):
		if self.load >= 100:
			self.interact()
			self.load = 0
		self.load += 1
			
	def get_load(self):
		return self.load
		
	def get_level(self):
		return self.level
		
	def upgrade_level(self):
		if self.level < 1:
			self.level += 1
		
	def reset_load(self):
		self.load = 0
		
	def interact(self):
		pass