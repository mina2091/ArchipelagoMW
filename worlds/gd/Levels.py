from typing import List, TypedDict
from BaseClasses import Item, ItemClassification

class LevelData(TypedDict):

	name: str
	id:str
	difficulty: int
	progress: int = 0		#when reaching certain amount hand out debuffs instead

	#easy			0
	#medium			1
	#hard			2
	#harder			3
	#insane			4
	#easy demon		5
	#medium demon	6
	#hard demon		7
	#insane demon	8
	#extreme demon	9

level_table: List[LevelData] = [
	{"name": "ReTraY", "id": "6508283", "difficulty": 0, "progress": 0}, 
	{"name": "The Nightmare", "id": "13519", "difficulty": 5, "progress": 0}
]