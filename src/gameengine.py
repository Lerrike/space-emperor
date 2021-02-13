import math
from commandership import CommanderShip
from homeplanet import HomePlanet
from moon import Moon

class GameEngine():
	def __init__(self, dt):
		self.dt = dt
		self.all_objects = []
		self.static_objects = []
		self.interactable = []
		self.ai_objects = []
		
		self.day = 1
		self.month = 1
		self.year = 3300
		self.date = [self.day, self.month, self.year]
		
		self.init_world()
		
	def init_world(self):
		self.commandership = CommanderShip(self.dt)
		self.all_objects.append(self.commandership)
		
		self.homeplanet = HomePlanet()
		self.all_objects.append(self.homeplanet)
		self.static_objects.append(self.homeplanet)
		self.homeplanet.init_(self)
		
		self.moon = Moon()
		self.all_objects.append(self.moon)
		self.static_objects.append(self.moon)
		
	def add_to_all_objects(self, object):
		self.all_objects.append(object)
		
	def add_to_interactable(self, object):
		self.interactable.append(object)
		
	def get_cs(self):
		return self.commandership
		
	def get_date(self):
		return [self.day, self.month, self.year]
		
	def get_objects(self):
		return self.all_objects
		
	def get_static_objects(self):
		return self.static_objects
		
	def get_interactable_objects(self):
		return self.interactable
		
	def get_ai_objects(self):
		return self.ai_objects
		
	def set_window(self, window):
		self.window = window
		
	def get_window(self):
		return self.window
	
	def update_world(self):
		is_set = 0
		for object in self.interactable:
			if self.in_closerange(self.commandership, object):
				self.commandership.set_object_in_closerange(object)
				is_set = 1
		if not is_set:
			self.commandership.set_object_in_closerange(0)
			
		
	def in_closerange(self, object1, object2):
		if math.dist(object1.get_pos(), object2.get_pos()) <= 30:
			return True
		else:
			return False
		
	def in_midrange(self, object1, object2):
		if math.dist(object1.get_pos(), object2.get_pos()) <= 720/2:
			return True
		else:
			return False
		
	def in_longrange(self, object1, object2):
		if math.dist(object1.get_pos(), object2.get_pos()) <= 100000:
			return True
		else:
			return False
			
		
	def tick_time(self):
		self.day += 1
		if self.day > 30:
			self.day = 1
			self.month += 1
		if self.month >= 12:
			self.month = 1
			self.year += 1
			
	def do_tick_action(self):
		basemine = self.homeplanet.get_basemine()
		if basemine.exists:
			self.homeplanet.get_basemine().increment_resource()
		
	def action(self):
		object = self.commandership.get_object_in_closerange()
		if object:
			cost = object.get_interaction_cost()
			is_possible = self.commandership.get_resources() > cost
			if is_possible:
				done = object.load_interaction(self)
				if done:
					self.commandership.use_resources(cost)
				
	def action_reset(self):
		object = self.commandership.get_object_in_closerange()
		if object:
			object.reset_load()