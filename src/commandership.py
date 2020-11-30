import math

class CommanderShip():
	def __init__(self,dt):
		self.dt = dt
		self.x = 0
		self.y = 0
		self.ang = 0 #90
		self.x_vel = 0
		self.y_vel = 0
		self.ang_vel = 0
		
		self.acc = 16*2
		
	def get_x(self):
		return self.x
		
	def get_y(self):
		return self.y
		
	def get_angle(self):
		return self.ang
		
	def get_x_vel(self):
		return self.x_vel
		
	def get_y_vel(self):
		return self.y_vel
		
	def get_ang_vel(self):
		return self.ang_vel
		
	def stop_rotation(self):
		self.ang_vel = 0
		
	def turn_left(self):
		self.ang_vel = -90
		
	def turn_right(self):
		self.ang_vel = 90
		
	def update_angle_position(self):
		self.update_angle()
		self.update_position()
		
	def update_angle(self):
		self.ang += self.ang_vel * self.dt
		if self.ang > 180:
			self.ang -= 360
		elif self.ang < -180:
			self.ang += 360
			
	def accelerate(self):
		#self.x_vel += math.cos(self.ang) * self.acc * self.dt
		#self.y_vel += math.sin(self.ang) * self.acc * self.dt
		self.x_vel = math.sin(math.radians(self.ang))*16*6
		self.y_vel = math.cos(math.radians(self.ang))*16*6
		
	def decelerate(self):
		self.x_vel = 0
		self.y_vel = 0
		
	def update_position(self):
		self.x += self.x_vel * self.dt
		self.y += self.y_vel * self.dt
		