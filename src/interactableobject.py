from generalspaceobject import GeneralSpaceObject

class InteractableObject(GeneralSpaceObject):
	def __init__(self, max, exists, x, y):
		super().__init__()
		self.name = "Nothing"
		self.intersection = "DoNothing"
		self.x = x
		self.y = y
		self.load = 0
		self.level = 0
		self.max_level = max
		self.exists = exists
		self.sprites = []
		self.costs = -1
		
	def get_name(self):
		return self.name
		
	def get_interaction_name(self):
		return self.interaction
		
	def get_sprite(self):
		return self.sprites[self.level]
		
	def set_level_sprite(self, sprite):
		self.sprites.append(sprite)
		
	def load_interaction(self, cs, date):
		if self.load >= 100:
			self.interact(cs, date)
			self.load = 0
			return True
		self.load += 1
		return False
		
	def get_interaction_cost(self):
		return self.costs[self.level]
			
	def get_load(self):
		return self.load
		
	def get_level(self):
		return self.level
		
	def set_level(self, level):
		self.level = level
		
	def upgrade_level(self):
		if self.level < self.max_level:
			self.level += 1
		
	def reset_load(self):
		self.load = 0
		
	def interact(self, cs):
		pass
		
	def set_exist(self, value):
		self.exists = value
		self.sprites[self.level].visible = value