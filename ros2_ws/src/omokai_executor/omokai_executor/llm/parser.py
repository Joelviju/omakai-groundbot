import json

from ..mission import Mission
from ..mission import Waypoint


def parse_mission(response: str) -> Mission:
    """
    Parse and validate an LLM-generated mission.
    """

    try:
        data = json.loads(response)

    except json.JSONDecodeError as e:
        raise ValueError(
            f"Invalid JSON returned by LLM:\n{response}"
        ) from e

    #
    # Required fields
    #
    required = [
        "mission_type",
        "laps",
        "speed",
        "waypoints",
    ]

    for field in required:

        if field not in data:

            raise ValueError(
                f"Missing required field '{field}'"
            )

    #
    # Validate mission_type
    #
    if data["mission_type"] != "patrol":

        raise ValueError(
            "Only 'patrol' missions are supported."
        )

    #
    # Validate laps
    #
    laps = int(data["laps"])

    if laps <= 0:

        raise ValueError(
            "laps must be greater than zero."
        )

    #
    # Validate speed
    #
    speed = float(data["speed"])

    if not (0.1 <= speed <= 1.0):

        raise ValueError(
            "speed must be between 0.1 and 1.0"
        )

    #
    # Validate waypoints
    #
    raw_waypoints = data["waypoints"]

    if len(raw_waypoints) == 0:

        raise ValueError(
            "Mission contains no waypoints."
        )

    waypoints = []

    for wp in raw_waypoints:

        for key in ["x", "y", "yaw"]:

            if key not in wp:

                raise ValueError(
                    f"Waypoint missing '{key}'"
                )

        waypoints.append(

            Waypoint(

                x=float(wp["x"]),

                y=float(wp["y"]),

                yaw=float(wp["yaw"]),

            )

        )

    return Mission(

        mission_type="patrol",

        laps=laps,

        speed=speed,

        waypoints=waypoints,

    )