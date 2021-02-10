import math
from mobilespaceobject import MobileSpaceObject

class CommanderShip(MobileSpaceObject):
	def __init__(self):
		super().__init__()
		self.object_in_closerange = 0
		
	def set_object_in_closerange(self, object):
		self.object_in_closerange = object
		
	def get_object_in_closerange(self):
		return self.object_in_closerange