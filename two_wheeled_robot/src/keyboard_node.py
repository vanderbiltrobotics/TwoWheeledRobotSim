#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import getch
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import keyboard


class MinimalPublisher(Node):
    def __init__(self):
        super().__init__("minimal_publisher")
        self.speed_publisher_ = self.create_publisher(Twist, "cmd_vel", 10)
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        speed_msg = Twist()
        speed_msg.linear.x = 0.0
        speed_msg.angular.z = 0.0
        k = ord(getch.getch())
        if k == 119:
            print("Up")
            speed_msg.linear.x = 1.0
        elif k == 97:
            print("Left")
            speed_msg.angular.z = 1.0
        elif k == 115:
            print("Back")
            speed_msg.linear.x = -1.0
        elif k == 100:
            print("Right")
            speed_msg.angular.z = -1.0
        else:
            print("Stop")
            speed_msg.linear.x = 0.0
            speed_msg.angular.z = 0.0
        self.speed_publisher_.publish(speed_msg)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

# def timer_callback(self):
#    k = ord(getch.getch())
#    print(k)
