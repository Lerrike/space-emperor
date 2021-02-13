from enum import Enum

class Side(Enum):
	Ally = 1
	Neutral = 2
	Enemy = 3
	
class EngineList(Enum):
	Null = 0
	Static = 1
	Interactable = 2
	AI = 3