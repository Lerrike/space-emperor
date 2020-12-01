from staticspaceobject import StaticSpaceObject

class HomePlanet(StaticSpaceObject):
	def __init__(self,dt):
		super().__init__(dt)
		self.x = 0
		self.y = 360