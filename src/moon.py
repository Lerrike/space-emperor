from staticspaceobject import StaticSpaceObject
from enumerations import *
from base import Base
from basemine import Basemine

class Moon(StaticSpaceObject):
	def __init__(self):
		super().__init__()
		self.x = 10000
		self.y = 160
		self.description = Description.Moon
		
		self.level = 0
		