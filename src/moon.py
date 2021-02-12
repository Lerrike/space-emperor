from staticspaceobject import StaticSpaceObject
from enumerations import *

class Moon(StaticSpaceObject):
	def __init__(self, all_objects_list, interactable_list):
		super().__init__()
		self.x = 1000
		self.y = 160
		self.description = Description.Moon
		
		self.level = 0
		
		self.all_objects_list = all_objects_list
		self.interactable_list = interactable_list
		