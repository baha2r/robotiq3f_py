# robotiq_3f_gripper
Control robotiq 3f gripper using modbus client

# Control
Using GripperController class, you can control the gripper with different modes, different speeds or different force applied. 
Also, you can control each finger invidially.

# Installation
The only package you need is pyModbusTCP, which can be installed with: `pip install pyModbusTCP`

Create a ethernet connection, select the manual option for the method and set the IPv4 settings to the following values:

i. Address: 192.168.1.2

ii. Netmask: 255.255.255.0

iii. Gateway: 0.0.0.0

![Ethernet_IPv4](https://github.com/baha2r/robotiq_3f_gripper/assets/75396051/2caa843d-18e1-429f-a00c-29b129244c32)

# Test
Run the main.py
