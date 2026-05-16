# Check installed packages
dpkg -l | grep -E "ros-jazzy-navigation2|ros-jazzy-nav2-bringup|ros-jazzy-vision-msgs|python3-opencv|python3-yaml"

# Install missing dependencies
sudo apt update

for pkg in \
    ros-jazzy-navigation2 \
    ros-jazzy-nav2-bringup \
    ros-jazzy-vision-msgs \
    python3-opencv \
    python3-yaml
do
    if dpkg -s $pkg >/dev/null 2>&1; then
        echo "$pkg is already installed"
    else
        echo "Installing $pkg..."
        sudo apt install -y $pkg
    fi
done

# verify
ros2 pkg list | grep -E "nav2|vision_msgs"
python3 -c "import cv2; print(cv2.__version__)"
python3 -c "import yaml; print('PyYAML OK')"

#Source ROS2
source /opt/ros/jazzy/setup.bash

#verify
echo $ROS_DISTRO

#build the workspace
colcon build --symlink-install


