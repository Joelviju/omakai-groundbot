from pathlib import Path

import rclpy
from rclpy.node import Node

from .mission_generator import MissionGenerator
from .mission_loader import MissionLoader
from .nav_client import NavClient


class MissionExecutor(Node):
    """
    Deterministic Mission Executor.

    Supports two modes:

    1. Mission JSON file
    2. Natural-language prompt
    """

    def __init__(self):

        super().__init__("mission_executor")

        project_root = Path.cwd().parent

        default_mission = (
            project_root
            / "missions"
            / "warehouse_loop.json"
        )

        #
        # Parameters
        #
        self.declare_parameter(
            "mission_file",
            str(default_mission),
        )

        self.declare_parameter(
            "prompt",
            "",
        )

        mission_file = (
            self.get_parameter("mission_file")
            .get_parameter_value()
            .string_value
        )

        prompt = (
            self.get_parameter("prompt")
            .get_parameter_value()
            .string_value
        )

        #
        # Generate mission from prompt OR load JSON
        #
        if prompt != "":

            self.get_logger().info(
                f'Generating mission from prompt: "{prompt}"'
            )

            generator = MissionGenerator()

            mission = generator.generate(prompt)

        else:

            self.get_logger().info(
                f"Loading mission: {mission_file}"
            )

            mission = MissionLoader.load(
                mission_file
            )

        self.get_logger().info(
            "Mission loaded successfully!"
        )

        self.get_logger().info(str(mission))

        #
        # Navigation client
        #
        self.nav = NavClient(self)

        self.nav.wait_until_ready()

        #
        # Execute mission
        #
        for lap in range(mission.laps):

            self.get_logger().info(
                f"========== LAP {lap + 1}/{mission.laps} =========="
            )

            for waypoint in mission.waypoints:

                self.nav.navigate_to_pose(
                    waypoint.x,
                    waypoint.y,
                    waypoint.yaw,
                )

        self.get_logger().info(
            "Mission completed!"
        )


def main(args=None):

    rclpy.init(args=args)

    executor = MissionExecutor()

    executor.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()