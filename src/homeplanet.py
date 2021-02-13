from staticspaceobject import StaticSpaceObject
from base import Base
from basemine import Basemine
from builderfactory import BuilderFactory
from enumerations import *

class HomePlanet(StaticSpaceObject):
	def __init__(self):
		super().__init__()
		self.x = 0
		self.y = 160
		self.description = Description.Homeplanet
		
		self.level = 0
		
		
	def init_(self, engine):
		self.base = Base(6, self.x,self.y, self)
		engine.add_to_all_objects(self.base)
		engine.add_to_interactable(self.base)
		
		self.basemine = Basemine(0,self.x,self.y + 180)
		self.basemine.set_level(0)
		
		self.factory = BuilderFactory(0,self.x + 180,self.y)
		self.factory.set_level(0)
		
	def get_level(self):
		return self.base.get_level()
		
	def get_base(self):
		return self.base
		
	def get_basemine(self):
		return self.basemine
		
	def level_action(self, engine):
		level = self.base.get_level()
		if level == 1:
			self.basemine.set_exist(True, self.basemine, engine)
			engine.add_to_interactable(self.basemine)
			self.factory.set_exist(True, self.factory, engine)
			engine.add_to_interactable(self.factory)
		
