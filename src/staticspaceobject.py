import math
from generalspaceobject import GeneralSpaceObject
from enumerations import *

class StaticSpaceObject(GeneralSpaceObject):
	def __init__(self):
		super().__init__()
		self.description = EngineList.Static
	