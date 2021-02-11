import math

class Camera():
	def __init__(self, x_center, y_center, size, scaling):
		self.size = size
		self.scaling = scaling
		self.x = 0
		self.y = 0
		self.x_center = x_center
		self.y_center = y_center
		self.angle = 0
		
	def get_size(self):
		return self.size
		
	def get_position(self):
		return [self.x, self.y]
		
	def get_center(self):
		return [self.x_center, self.y_center]
		
	def update_camera_posang(self, x_cs, y_cs, angle):
		self.x = x_cs
		self.y = y_cs
		self.angle = angle
		
	def scale(self, value):
		return value/self.scaling
		
	def get_posang_in_view(self, x, y, angle):
		angle_view = angle - self.angle
		dx = x - self.x
		dy = y - self.y
		ang_rel = math.atan2(dy,dx)
		#angle = math.radians(angle)
		dang = ang_rel + math.radians(self.angle)
		L = math.sqrt(dx**2+dy**2)
		L = self.scale(L)
		x_view = self.x_center + L*math.cos(dang)
		y_view = self.y_center + L*math.sin(dang)
		return x_view, y_view, angle_view
		
	def is_on_view(self, object):
		return 1