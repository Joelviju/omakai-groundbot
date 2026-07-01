import math
from threading import Event

from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient


class NavClient:
    """
    Simple blocking wrapper around Nav2.

    MissionExecutor simply calls:

        navigate_to_pose(...)

    and waits until the robot reaches the goal.
    """

    def __init__(self, node):

        self.node = node

        self.client = ActionClient(
            node,
            NavigateToPose,
            "navigate_to_pose",
        )

        self.goal_done = Event()

    def wait_until_ready(self):

        self.node.get_logger().info(
            "Waiting for Nav2 action server..."
        )

        self.client.wait_for_server()

        self.node.get_logger().info(
            "Nav2 is ready!"
        )

    def navigate_to_pose(self, x, y, yaw):

        self.goal_done.clear()

        goal = NavigateToPose.Goal()

        pose = PoseStamped()

        pose.header.frame_id = "map"
        pose.header.stamp = self.node.get_clock().now().to_msg()

        pose.pose.position.x = float(x)
        pose.pose.position.y = float(y)
        pose.pose.position.z = 0.0

        pose.pose.orientation.z = math.sin(yaw / 2.0)
        pose.pose.orientation.w = math.cos(yaw / 2.0)

        goal.pose = pose

        self.node.get_logger().info(
            f"Navigating to ({x}, {y})"
        )

        future = self.client.send_goal_async(goal)

        future.add_done_callback(
            self.goal_response_callback
        )

        #
        # Wait until the robot reaches the goal
        #
        while not self.goal_done.is_set():

            import rclpy

            rclpy.spin_once(
                self.node,
                timeout_sec=0.1,
            )

    def goal_response_callback(self, future):

        goal_handle = future.result()

        if not goal_handle.accepted:

            self.node.get_logger().error(
                "Goal rejected!"
            )

            self.goal_done.set()

            return

        self.node.get_logger().info(
            "Goal accepted."
        )

        result_future = goal_handle.get_result_async()

        result_future.add_done_callback(
            self.result_callback
        )

    def result_callback(self, future):

        self.node.get_logger().info(
            "Goal completed."
        )

        self.goal_done.set()