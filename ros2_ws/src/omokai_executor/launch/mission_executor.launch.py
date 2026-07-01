from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        DeclareLaunchArgument(
            "mission_file",
            default_value="/omakai-groundbot/missions/warehouse_loop.json",
        ),

        DeclareLaunchArgument(
            "prompt",
            default_value="",
        ),

        Node(
            package="omokai_executor",
            executable="executor",
            name="mission_executor",
            output="screen",
            parameters=[
                {
                    "mission_file": LaunchConfiguration("mission_file"),
                    "prompt": LaunchConfiguration("prompt"),
                }
            ],
        ),
    ])