from enum import Enum

class Side(Enum):
	Ally = 1
	Neutral = 2
	Enemy = 3
	
class Description(Enum):
	Null = 0
	Homeplanet = 1
	Moon = 2
	Asteroid = 3
	Hostilebase = 4