import math
from mobilespaceobject import MobileSpaceObject

class CommanderShip(MobileSpaceObject):
	def __init__(self, created):
		super().__init__(created)
		self.object_in_closerange = 0
		self.max_resources = 1000
		self.resources = 52
		
	def get_object_in_closerange(self):
		return self.object_in_closerange
		
	def set_object_in_closerange(self, object):
		self.object_in_closerange = object
		
	def get_max_resources(self):
		return self.max_resources
		
	def has_resources(self):
		if self.resources > 0:
			return True
		else:
			return False
		
	def acc_action(self):
		self.acc = 4
		self.resources -= 0.02
		
	def decelerate(self):
		self.acc = -2
		self.resources -= 0.01
		
	def turn_left(self):
		self.ang_vel = -30
		self.resources -= 0.001
		
	def turn_right(self):
		self.ang_vel = 30
		self.resources -= 0.001
		return True
		
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