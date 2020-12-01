import math
from generalspaceobject import GeneralSpaceObject

class MobileSpaceObject(GeneralSpaceObject):
	def __init__(self,dt):
		super().__init__(dt)
		self.x_vel = 0
		self.y_vel = 0
		self.ang_vel = 0
		self.acc = 0
		
	def get_x_vel(self):
		return self.x_vel
		
	def get_y_vel(self):
		return self.y_vel
		
	def get_ang_vel(self):
		return self.ang_vel
		
	def update_angle_position(self):
		self.update_angle()
		self.update_position()
		
	def update_position(self):
		self.update_speed()
		self.x += self.dt * self.x_vel
		self.y += self.dt * self.y_vel 
		
	def update_speed(self):
		if self.acc >= 0:
			self.x_vel += math.sin(math.radians(self.ang)) * self.acc * self.dt
			self.y_vel += math.cos(math.radians(self.ang)) * self.acc * self.dt
		else:
			angle_of_velocity = math.atan2(self.y_vel,self.x_vel)
			if math.fabs(self.x_vel) > 1:
				self.x_vel += math.cos(angle_of_velocity) * self.acc * self.dt
			else:
				self.x_vel = 0
			if math.fabs(self.y_vel) > 1:
				self.y_vel += math.sin(angle_of_velocity) * self.acc * self.dt
			else:
				self.y_vel = 0
				
	def update_angle(self):
		self.ang += self.ang_vel * self.dt
		if self.ang > 180:
			self.ang -= 360
		elif self.ang < -180:
			self.ang += 360
			
	def stop_rotation(self):
		self.ang_vel = 0
		
	def turn_left(self):
		self.ang_vel = -45
		
	def turn_right(self):
		self.ang_vel = 45
		
			
	def acc_action(self):
		self.acc = 16*2 
		
	def no_acc_action(self):
		self.acc = 0
		
	def decelerate(self):
		self.acc = -16*2