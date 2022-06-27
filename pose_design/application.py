from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

import sys

from pose_design.my_widgets import MySlider, Point

joints_names = ['HeadYaw', 'HeadPitch', 'LShoulderPitch', 'LShoulderRoll', 'LElbowYaw',
                'LElbowRoll', 'LWristYaw', 'LHipYawPitch', 'LHipRoll', 'LHipPitch',
                'LKneePitch', 'LAnklePitch', 'LAnkleRoll', 'RHipRoll', 'RHipPitch',
                'RKneePitch', 'RAnklePitch', 'RAnkleRoll', 'RShoulderPitch', 'RShoulderRoll',
                'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'LHand', 'RHand']
joints_ranges = [range(-115, 115)]


class Joint:
    def __init__(self, name, range_list, slider):
        self.num = joints_names.index(name)
        self.name = name
        self.range = joints_ranges[self.num]  # degrees
        self.slider = slider

    def getValue(self):
        return self.slider.value()

    def setValue(self, value):
        self.slider.set(value)


class Window(QMainWindow):
    def __init__(self, receive, send):
        super(Window, self).__init__()

        self.send = send
        self.receive = receive
        self.setWindowTitle("Simple program")
        self.setGeometry(1000, 250, 600, 350)  # (300, 250) от левого верхнего угла
        # ширина, высота

        self.buttons = self.make_buttons()

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Hello")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.sliders = self.make_sliders()
        self.joints = self.make_joints()

    def make_buttons(self):
        class Buttons:
            apply = self.make_button('Apply', Point(50, 300))
            send_pose = self.make_button('Send Pose', Point(250, 300), self.send)
            receive_pose = self.make_button('Receive Pose', Point(450, 300), self.receive)

        return Buttons
        # return {'apply': button_apply, 'receive': button_receive_pose, 'send': button_send_pose}

    def make_button(self, name='Test button', point=Point(), signal=None):
        btn = QtWidgets.QPushButton(self)
        btn.move(point.x, point.y)
        btn.setText(name)
        btn.adjustSize()
        if signal is not None:
            btn.clicked.connect(signal)
        return btn

    def make_sliders(self):
        class Sliders:
            SldHeadYaw = self.make_slider(name='HeadYaw', point=Point(200, 100),
                                          sld_range=joints_ranges[joints_names.index('HeadYaw')])

        return Sliders

    def make_slider(self, name='Test slider', point=Point(), sld_range=range(0, 1)):
        sld = MySlider(self, self.buttons.apply, Point(point.x, point.y), sld_range, name)
        return sld

    def getPose(self):
        pose = [0] * 25
        for joint in self.JointsList:
            pose[joint.num] = joint.getValue()
        return pose

    def setPose(self, pose):
        for joint in self.JointsList:
            joint.setValue(pose[joint.num])



    def make_joints(self):
        class Joints:
            HeadYaw = Joint(name=self.sliders.SldHeadYaw.name,
                            range_list=self.sliders.SldHeadYaw.slider_range, slider=self.sliders.SldHeadYaw)

        self.JointsList = [Joints.HeadYaw]
        return Joints


'''def Application(send, receive):
    app = QApplication(sys.argv)
    window = Window(send, receive)
    window.show()
    sys.exit(app.exec_())  # корректное завершение'''



'''
if __name__ == "__main__":
    application()'''
