import json

from .mission import Mission, Waypoint


class MissionLoader:

    @staticmethod
    def load(filename: str) -> Mission:

        with open(filename, "r") as f:
            data = json.load(f)

        waypoints = []

        for wp in data["waypoints"]:

            waypoints.append(
                Waypoint(
                    x=wp["x"],
                    y=wp["y"],
                    yaw=wp["yaw"],
                )
            )

        return Mission(
            mission_type=data["mission_type"],
            laps=data["laps"],
            speed=data["speed"],
            waypoints=waypoints,
        )