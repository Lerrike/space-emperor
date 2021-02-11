from interactableobject import InteractableObject

class Base(InteractableObject):
	def __init__(self, x, y, homeplanet):
		super().__init__()
		self.x = x
		self.y = y
		self.homeplanet = homeplanet
		
		self.sprites = []
		self.costs = [0,5,12,25,45,70,100]
		
	def get_sprite(self):
		return self.sprites[self.homeplanet.get_level()]
		
	def set_level_sprite(self, sprite):
		self.sprites.append(sprite)
		
	def interact(self):
		self.upgrade_level()
		self.sprites[self.level-1].visible = False
		self.sprites[self.level].visible = True
		
	def get_cost(self):
		pass