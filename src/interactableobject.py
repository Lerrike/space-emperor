from generalspaceobject import GeneralSpaceObject

class InteractableObject(GeneralSpaceObject):
	def __init__(self, x, y):
		super().__init__()
		self.x = x
		self.y = y
		self.in_closerange = False
		
	def is_in_closerange(self):
		return self.in_closerange
		
	def set_in_closerange(self, value):
		self.in_closerange = value