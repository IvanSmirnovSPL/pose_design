#How to install
cd ~/dev_ws
git clone https://github.com/IvanSmirnovSPL/pose_design.git /src/pose_design
colcon build --packages-select pose_design
. install/setup.bash

#How to run (another terminal)
. install/setup.bash
ros2 run pose_design PoseDesign
