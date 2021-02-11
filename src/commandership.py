import math
from mobilespaceobject import MobileSpaceObject

class CommanderShip(MobileSpaceObject):
	def __init__(self):
		super().__init__()
		self.object_in_closerange = 0
		self.max_resources = 100
		self.resources = 100
		
	def get_object_in_closerange(self):
		return self.object_in_closerange
		
	def set_object_in_closerange(self, object):
		self.object_in_closerange = object
		
	def get_max_resources(self):
		return self.max_resources
		
	def get_resources(self):
		return self.resources
		
	def add_resources(self, amount):
		if self.resources + amount > self.max_resources:
			over = self.resources + amount - self.max_resources
			self.resources = self.max_resources
			return over
		else:
			self.resources += amount
			return 0
			
	def use_resources(self, amount):
		if self.resources - amount < 0:
			return 0
		else:
			self.resources -= amount
			return 1