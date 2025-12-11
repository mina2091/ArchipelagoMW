from typing import List, TypedDict
from BaseClasses import Location

class LocationInfo(TypedDict):
    name: str
    id: int
    progress: int

location_table: List[LocationInfo] = [
    {"name": "ReTraY Completion", "id": "6508283", "difficulty": 0, "progress": 1},
    {"name": "The Nightmare Completion", "id": "13519", "difficulty": 5, "progress": 1},
]