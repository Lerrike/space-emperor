from staticspaceobject import StaticSpaceObject
from base import Base

class HomePlanet(StaticSpaceObject):
	def __init__(self, all_objects_list, interactable_list):
		super().__init__()
		self.x = 0
		self.y = 360
		
		self.level = 0
		self.level_sprites = []
		
		self.base = Base(self.x,self.y, self)
		all_objects_list.append(self.base)
		interactable_list.append(self.base)
		
	def get_level(self):
		return self.base.get_level()
		
	def get_base(self):
		return self.base
		
