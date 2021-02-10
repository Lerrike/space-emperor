from interactableobject import InteractableObject

class Base(InteractableObject):
	def __init__(self, x, y, homeplanet):
		super().__init__()
		self.x = x
		self.y = y
		self.homeplanet = homeplanet
		
		self.sprites = []
		
	def get_sprite(self):
		return self.sprites[self.homeplanet.get_level()]
		
	def set_level_sprite(self, sprite):
		self.sprites.append(sprite)
		
	def interact(self):
		self.homeplanet.upgrade_level()
		level = self.homeplanet.get_level()
		self.sprites[level-1].visible = False
		self.sprites[level].visible = True