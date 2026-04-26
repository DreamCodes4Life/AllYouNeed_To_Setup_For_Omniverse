
Prepare your PC with Ubuntu 22 or above

# 1) Install VSCode

```bash
  sudo apt update
  sudo apt install software-properties-common apt-transport-https wget -y
  wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
  sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
  sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
  sudo apt update
  sudo apt install code
```

# 2) Python 3 Setup on Ubuntu

```bash
# Check if Python 3 is installed
python3 --version || echo "Python3 not installed"

# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install python3 python3-pip -y

# Verify installation
python3 --version
pip3 --version

# Test Python
python3 -c "print('Hello, Python is working!')"
```

# 3) Install NVIDIA Drivers

🔗 [NVIDIA Drivers official page:](https://www.nvidia.com/en-us/drivers/)
 

```bash
  nvidia-smi
  ubuntu-drivers devices
  sudo ubuntu-drivers autoinstall
  sudo apt install nvidia-driver-580-open
```

# 4) Install Docker y NVIDIA Tool Kit

🔗 [Install Docker y NVIDIA Docker Tool Kit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)


# 5) Install Kit App Template
🔗 [Repo](https://github.com/NVIDIA-Omniverse/kit-app-template)

## 5.1) Build and Navigate USDComposer
🔗 [Overview USDComposer](https://docs.omniverse.nvidia.com/composer/latest/interface.html)

## 5.2) USDExplorer
Seguid mismos pasos que con USDComposer pero elegir USDExplorer

# 6) Install IsaacSim
🔗 [Download IsaacSim](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/installation/download.html)

## 6.1) Build your first Robot
🔗 [Tutorial to build your first robot](https://docs.nvidia.com/learning/physical-ai/getting-started-with-isaac-sim/latest/building-your-first-robot-in-isaac-sim/index.html)

# 7) Install ROS2 and RVIZ
🔗 [Download IsaacSim](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/installation/install_ros.html)

## 7.1) Tutorial IsaacSim ROS2
🔗 [Download IsaacSim](https://www.youtube.com/watch?v=F9K7RUmumQc)

# 8) OpenUSD y Tutoriales
🔗 [Open USD Learning and tutorials](https://docs.nvidia.com/learn-openusd/latest/index.html)
🔗 [Open USD Explained in my Github](https://github.com/DreamCodes4Life/OpenUSDFundamentals)
🔗 [Youtube PlayList](https://www.youtube.com/watch?v=ulZMQLSNgyQ&list=PL5DeJbWGvSbevfX8PaqGpWImnVxT2BIKd)

# Documents and tutorials to follow
In the bellow link you have all details about IsaacSim, tutorials, ROS2, IsaacLab, etc. 
NOTE: if you switch between versions you can find different tutorials.
🔗 [All About IsaacSim](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/index.html)







