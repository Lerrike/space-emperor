import math
from generalspaceobject import GeneralSpaceObject

class MobileSpaceObject(GeneralSpaceObject):
	def __init__(self,dt):
		super().__init__()
		self.x_vel = 0
		self.y_vel = 0
		self.ang_vel = 0
		self.acc = 0
		
		self.max_resources = 0
		self.resources = 0
		self.max_acc_thrust = 10
		self.max_dec_thrust = 5
		self.max_ang_vel = 30
		
		
		self.dt = dt
		
	def get_velocity(self):
		return [self.x_vel, self.y_vel]
	
	def get_x_vel(self):
		return self.x_vel
		
	def get_y_vel(self):
		return self.y_vel
		
	def get_ang_vel(self):
		return self.ang_vel
		
	def get_acc(self):
		return self.acc
		
	def get_max_acc(self):
		return self.max_acc_thrust
		
	def get_max_dec(self):
		return self.max_dec_thrust
		
	def use_energy(self):
		acc = math.fabs(self.acc)
		torque = math.fabs(self.ang_vel)
		consumption = acc/1000 + torque/10000
		self.resources -= consumption
		
	def total_velocity(self):
		velocity = math.sqrt(self.x_vel**2 + self.y_vel**2)
		return velocity
		
	def dv(self, acc):
		return acc*self.dt
		
	def v_steps_to_zero(self, thrust):
		v_tot = self.total_velocity()
		dv = self.dv(thrust)
		return v_tot/dv
		
		
	def optimal_brakepoint_distance(self, thrust):
		dv = self.dv(thrust)
		n = self.v_steps_to_zero(thrust)
		n = math.floor(n)
		dx = 0
		#for i in range(steps):
		#	speed_step = self.total_velocity() - i * dv
		#	dx += self.dt * speed_step
		v_tot = self.total_velocity()
		dx = self.dt * (n * v_tot - dv * n*(n-1)/2)
		return dx
		
	def acc_dec_difference(self):
		return self.max_acc_thrust/self.max_dec_thrust
		
	def update_angle_position(self):
		self.update_angle()
		self.update_position()
		
	def update_position(self):
		self.update_speed()
		self.x += self.dt * self.x_vel
		self.y += self.dt * self.y_vel 
		
	def update_speed(self):
		dv_min = self.max_dec_thrust * self.dt
		if self.acc >= 0:
			self.x_vel += math.sin(math.radians(self.angle)) * self.acc * self.dt
			self.y_vel += math.cos(math.radians(self.angle)) * self.acc * self.dt
		else:
			angle_of_velocity = math.atan2(self.y_vel,self.x_vel)
			if math.fabs(self.x_vel) > dv_min:
				self.x_vel += math.cos(angle_of_velocity) * self.acc * self.dt
			else:
				self.x_vel = 0
			if math.fabs(self.y_vel) > dv_min:
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