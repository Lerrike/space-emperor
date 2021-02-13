from intelligentmobileobject import IntelligentMobileObject
from enumerations import *

class EngineerUnit(IntelligentMobileObject):
	def __init__(self, dt):
		super().__init__(dt)
		self.object_in_closerange = 0
		self.max_resources = 5000
		self.max_acc_thrust = 200
		self.max_dec_thrust = 100
		self.max_ang_vel = 200
		self.descrition = EngineList.AI