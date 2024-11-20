#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Pose
from gazebo_msgs.msg import ModelState

class MoveObject:
    def __init__(self):
        rospy.init_node('move_object_node_big', anonymous=True)
        self.object_pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)

    def move_to_position(self, x, y, z):
    
        object_state = ModelState()
        object_state.model_name = "small_ball_red"
        object_state.pose.position.x = x
        object_state.pose.position.y = y
        object_state.pose.position.z = z

        object_state.pose.orientation.w = 1.0
        object_state.twist.linear.x = 0.0
        object_state.twist.linear.y = 0.0
        object_state.twist.linear.z = 0.0
        object_state.twist.angular.x = 0.0
        object_state.twist.angular.y = 0.0
        object_state.twist.angular.z = 0.0
        object_state.reference_frame = "world"  

        self.object_pub.publish(object_state)
        rospy.loginfo("Nesne belirtilen konuma taşındı.")

if __name__ == '__main__':
    try:

        move_object_node = MoveObject()
         
        x = 7.5
        y = -6.5
        z = 7.0
        pay = 0.01
        while 1==1:    
            ########(y,z)
            # (-7.5,7) - (4.5,7) aralığı
            while y >= -7.5 :
                y = y + pay
                z = 7
                x = 7.5
                move_object_node.move_to_position(x, y, z)
                if y >= 4.5:
                    break

            # (4.5,7) - (4.5,4) aralığı
            while z <= 7 :
                z = z - pay
                y = 4.5
                x = 7.5
                move_object_node.move_to_position(x, y, z)
                if z <= 4:
                    break

            # (4.5,4) - (-7.5,4) aralığı
            while y <= 4.5 :
                y = y - pay
                z = 4
                x = 7.5
                move_object_node.move_to_position(x, y, z)
                if y <= -7.5:
                    break

            # (-7.5,4) - (-7.5,1) aralığı
            while z <= 4 :
                z = z - pay
                y = -7.5
                x = 7.5
                move_object_node.move_to_position(x, y, z)
                if z <= 1:
                    break

            # (-7.5,1) - (-6.5,1) aralığı
            while y >= -7.5 :
                y = y + pay
                z = 1
                x = 7.5
                move_object_node.move_to_position(x, y, z)
                if y >= -6.5:
                    break

            # (-6.5,1) - (-6.5,2) aralığı
            while z >= 1 :
                z = z + pay
                y = -6.5
                x = 7.5
                move_object_node.move_to_position(x, y, z)
                if z >= 2:
                    break
                
            # (-6.5,2) - (7.5,2) aralığı
            while y >= -6.5:
                y = y + pay
                z = 2
                x = 7.5
                move_object_node.move_to_position(x, y, z)
                if y >= 7.5:
                    break

            # (7.5,2) - (7.5,10) aralığı
            while z >= 2:
                z = z + pay
                y = 7.5
                x = 7.5
                move_object_node.move_to_position(x, y, z)
                if z >= 10:
                    break
            
            # (7.5,10) - (-7.5,10) aralığı    
            while y <= 7.5 :
                y = y - pay
                z = 10
                x = 7.5
                move_object_node.move_to_position(x, y, z)
                if y <= -7.5:
                    break
                
            # (-7.5,10) - (-7.5,7) aralığı    
            while z <= 10:
                z = z - pay
                y = -7.5
                x = 7.5
                move_object_node.move_to_position(x, y, z)
                if z <= 7:
                    break
                
            

        # move_object_node.move_to_position(x, y, z)

    except rospy.ROSInterruptException:
        pass
