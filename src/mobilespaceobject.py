import math
from generalspaceobject import GeneralSpaceObject

class MobileSpaceObject(GeneralSpaceObject):
	def __init__(self):
		super().__init__()
		self.x_vel = 0
		self.y_vel = 0
		self.ang_vel = 0
		self.acc = 0
		
		self.mass = 0
		self.max_resources = 0
		self.resources = 0
		
		self.dt = 1/15.0
		
		
	def get_mass(self):
		return self.mass
	
	def get_x_vel(self):
		return self.x_vel
		
	def get_y_vel(self):
		return self.y_vel
		
	def get_ang_vel(self):
		return self.ang_vel
		
	def get_acc(self):
		return self.acc
		
	def use_energy(self):
		force = math.fabs(self.mass * self.acc)
		torque = math.fabs(self.ang_vel)
		consumption = (force+torque)/20000
		self.resources -= consumption
		
	def update_angle_position(self):
		self.update_angle()
		self.update_position()
		
	def update_position(self):
		self.update_speed()
		self.x += self.dt * self.x_vel
		self.y += self.dt * self.y_vel 
		
	def update_speed(self):
		if self.acc >= 0:
			self.x_vel += math.sin(math.radians(self.angle)) * self.acc * self.dt
			self.y_vel += math.cos(math.radians(self.angle)) * self.acc * self.dt
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
		self.angle += self.ang_vel * self.dt
		if self.angle > 180:
			self.angle -= 360
		elif self.angle < -180:
			self.angle += 360
			
	def stop_rotation(self):
		self.ang_vel = 0
		
	def turn_left(self):
		self.ang_vel = -45
		
	def turn_right(self):
		self.ang_vel = 45
		
			
	def acc_action(self):
		self.acc = 2
		
	def no_acc_action(self):
		self.acc = 0
		
	def decelerate(self):
		self.acc = -2