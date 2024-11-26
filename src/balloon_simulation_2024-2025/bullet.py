#!/usr/bin/env python

import rospy
from gazebo_msgs.srv import SpawnModel, SetModelState
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose

class BasitTaret:
    def __init__(self):
        # ROS Node başlat
        rospy.init_node("basit_taret", anonymous=True)

        # Gazebo servislerini bekle
        rospy.wait_for_service('/gazebo/spawn_sdf_model')
        rospy.wait_for_service('/gazebo/set_model_state')

        # Servislere bağlan
        self.spawn_model = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
        self.set_model_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)

    def mermi_olustur(self, pozisyon):
        # Mermi model dosyasını oku
        with open("catkin_ws1/src/Camera-turret/camera_turret/models/bullet/model.sdf", "r") as f:
            mermi_sdf = f.read()

        # Mermi pozisyonu
        pose = Pose()
        pose.position.x = pozisyon[0]
        pose.position.y = pozisyon[1]
        pose.position.z = pozisyon[2]

        # Mermiyi spawn et
        model_adi = "mermi_{}".format(rospy.Time.now().to_nsec())
        try:
            self.spawn_model(model_name=model_adi,
                             model_xml=mermi_sdf,
                             robot_namespace="/",
                             initial_pose=pose,
                             reference_frame="world")
            rospy.loginfo("Mermi spawn edildi: %s" % model_adi)
        except rospy.ServiceException as e:
            rospy.logerr("Mermi spawn edilemedi: %s" % e)

        return model_adi

    def mermi_ates_et(self, model_adi, hız):
        # Mermi hareketini ayarla
        state_msg = ModelState()
        state_msg.model_name = model_adi
        state_msg.pose.position.x = 0
        state_msg.pose.position.y = 0
        state_msg.pose.position.z = 1
        state_msg.twist.linear.x = hız[0]
        state_msg.twist.linear.y = hız[1]
        state_msg.twist.linear.z = hız[2]

        try:
            self.set_model_state(state_msg)
            rospy.loginfo("Mermi ateşlendi!")
        except rospy.ServiceException as e:
            rospy.logerr("Mermi ateşlenemedi: %s" % e)

if __name__ == "__main__":
    taret = BasitTaret()
    while not rospy.is_shutdown():
        rospy.loginfo("Mermi atılıyor...")
        mermi_adi = taret.mermi_olustur([0, 0, 1])  # Başlangıç pozisyonu
        taret.mermi_ates_et(mermi_adi, [25, 0, 0])  # Hız vektörü (X yönünde hareket)
        rospy.sleep(2)  # 2 saniye bekle
