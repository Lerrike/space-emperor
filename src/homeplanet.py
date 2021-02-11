from staticspaceobject import StaticSpaceObject
from base import Base
from basemine import Basemine

class HomePlanet(StaticSpaceObject):
	def __init__(self, created, all_objects_list, interactable_list):
		super().__init__(created)
		self.x = 0
		self.y = 360
		
		self.level = 0
		self.level_sprites = []
		
		self.all_objects_list = all_objects_list
		self.interactable_list = interactable_list
		
		self.base = Base(created, 6, True, self.x,self.y, self)
		self.all_objects_list.append(self.base)
		self.interactable_list.append(self.base)
		
		self.basemine = Basemine(created, 0,False,self.x,self.y + 180)
		self.basemine.set_level(0)
		
	def get_level(self):
		return self.base.get_level()
		
	def get_base(self):
		return self.base
		
	def get_basemine(self):
		return self.basemine
		
	def level_action(self):
		level = self.base.get_level()
		if level == 1:
			self.basemine.set_exist(True)
			self.all_objects_list.append(self.basemine)
			self.interactable_list.append(self.basemine)
		
