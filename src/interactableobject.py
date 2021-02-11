from generalspaceobject import GeneralSpaceObject

class InteractableObject(GeneralSpaceObject):
	def __init__(self, max):
		super().__init__()
		self.load = 0
		self.level = 0
		self.max_level = max
		
	def load_interaction(self):
		if self.load >= 100:
			self.interact()
			self.load = 0
			return True
		self.load += 1
		return False
			
	def get_load(self):
		return self.load
		
	def get_level(self):
		return self.level
		
	def upgrade_level(self):
		if self.level < self.max_level:
			self.level += 1
		
	def reset_load(self):
		self.load = 0
		
	def interact(self):
		pass