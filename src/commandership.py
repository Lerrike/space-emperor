import math
from mobilespaceobject import MobileSpaceObject

class CommanderShip(MobileSpaceObject):
	def __init__(self, dt):
		super().__init__(dt)
		self.object_in_closerange = 0
		self.max_resources = 1000
		self.resources = 1000
		self.max_acc_thrust = 400
		self.max_dec_thrust = 200
		self.max_ang_vel = 200
		
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
		self.acc = self.max_acc_thrust
		self.use_energy()
		
	def decelerate(self):
		self.acc = -self.max_dec_thrust
		self.use_energy()
		
	def turn_left(self):
		self.ang_vel = -self.max_ang_vel
		self.use_energy()
		
	def turn_right(self):
		self.ang_vel = self.max_ang_vel
		self.use_energy()
		
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