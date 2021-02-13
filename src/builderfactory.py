from interactableobject import InteractableObject
from engineerunit import EngineerUnit

class BuilderFactory(InteractableObject):
	def __init__(self, max, x, y):
		super().__init__(max, x, y)
		self.name = "Builder Factory"
		self.interaction = "Make a Engineering Unit"
		self.costs = [25]
		self.angle = 90
		
	def interact(self, engine):
		unit = EngineerUnit(engine.dt)
		pos = self.get_pos()
		unit.set_pos(pos)
		engine.get_window().add_engineerunit(unit)
		engine.get_objects().append(unit)
		engine.get_ai_objects().append(unit)