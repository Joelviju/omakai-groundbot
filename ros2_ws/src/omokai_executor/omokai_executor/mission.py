from dataclasses import dataclass
from typing import List


@dataclass
class Waypoint:
    x: float
    y: float
    yaw: float


@dataclass
class Mission:
    mission_type: str
    laps: int
    speed: float
    waypoints: List[Waypoint]