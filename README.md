
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

# 2) 🐍 Python 3 Setup on Ubuntu

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


# 4) Install Docker

# 5) Install Kit App Template

## 5.1) Build USDComposer

### 5.1.1) Build your first Stage

## 5.2) Build USDExplorer

# 6) Install IsaacSim

## 6.1) Build your first Robot

# 7) Install ROS2 and RVIZ

## 7.1) Test coms with IsaacSim
