import math

class Camera():
	def __init__(self, width, height):
		self.size = height
		self.x = 0
		self.y = 0
		self.x_base = (width-height)/2 + self.size/2
		self.y_base = self.size/2
		print(self.x_base, self.y_base)
		self.angle = 0
		
	def update_camera_posang(self, x_cs, y_cs, angle):
		self.x = x_cs
		self.y = y_cs
		self.angle = angle
		
	def get_posang_in_view(self, x, y, angle):
		angle_view = angle - self.angle
		dx = x - self.x
		dy = y - self.y
		ang_rel = math.atan2(dy,dx)
		#angle = math.radians(angle)
		dang = ang_rel + math.radians(self.angle)
		L = math.sqrt(dx**2+dy**2)
		x_view = self.x_base + L*math.cos(dang)
		y_view = self.y_base + L*math.sin(dang)
		return x_view, y_view, angle_view