from staticspaceobject import StaticSpaceObject

class HomePlanet(StaticSpaceObject):
	def __init__(self):
		super().__init__()
		self.x = 0
		self.y = 360
		
		self.level = 0
		self.level_sprites = []
		
	def get_level(self):
		return self.level
		
	def get_level_sprites(self):
		return self.level_sprites
		
	def upgrade_level(self):
		if level < 6:
			self.level += 1
			
	def add_level_sprite(self, lvl, sprite):
		self.level_sprites.append([lvl, sprite])