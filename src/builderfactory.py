from interactableobject import InteractableObject
from engineerunit import EngineerUnit
from enumerations import *

class BuilderFactory(InteractableObject):
	def __init__(self, max, x, y):
		super().__init__(max, x, y)
		self.name = "Builder Factory"
		self.interaction = "Make a Engineering Unit"
		self.costs = [25]
		self.angle = 90
		
	def interact(self, engine):
		unit = EngineerUnit(engine.dt)
		engine.get_window().add_engineerunit(unit)
		unit.set_exist(True, engine)
		unit.set_pos(self.get_pos())