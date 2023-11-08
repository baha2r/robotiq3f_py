```markdown
# robotiq3f_py

Control the Robotiq 3F gripper using Python and a Modbus TCP client. This library provides a straightforward interface to integrate the Robotiq 3F gripper into your automation projects, allowing for various modes of operation, speed adjustments, and individual finger control.

## Features

- **Multiple Modes**: Operate the gripper in Basic, Pinch, Wide, and Scissor modes.
- **Speed and Force Control**: Fine-tune the speed and force applied by the gripper for delicate or robust operations.
- **Individual Finger Control**: Manage each finger separately for precise object manipulation.

## Installation

Before you begin, ensure you have Python installed on your system. Then, follow these steps to install the necessary dependencies:

```bash
pip install pyModbusTCP
```

## Setting Up

To establish a connection with the gripper, configure your Ethernet connection with the following IPv4 settings:

- Address: 192.168.1.2
- Netmask: 255.255.255.0
- Gateway: 0.0.0.0

## Usage

Import and initialize the `GripperController` class with the IP address of your Modbus server:

```python
from robotiqcontrol import GripperController

# Initialize the controller with the server IP
gripper = GripperController("192.168.1.11")

# Activate the gripper
gripper.activate()
```

## Examples

Here are some examples of how to use the `GripperController`:

### Basic Mode

```python
# Set the gripper to Basic Mode with default speed and force
gripper.command_gripper(rMOD="Basic")
```

### Individual Finger Control

```python
# Control each finger individually
gripper.command_gripper(rPRA=[255, 255, 255], rMOD="Pinch", rICF=True)
```

## Testing

To test the functionality, run the `test.py` script:

```bash
python test.py
```

## Troubleshooting

If you encounter any issues, please check the following:

- Ensure the gripper is powered and connected to the network.
- Verify the IP address and port settings.
- Check the Modbus server status.

For more detailed troubleshooting, please refer to the [issues section](https://github.com/baha2r/robotiq3f_py/issues) of this repository.

## Contribution

Contributions to improve `robotiq3f_py` are welcome! Please read our [contribution guidelines](CONTRIBUTING.md) before submitting a pull request.

## Support

For additional support or questions, please open an [issue](https://github.com/baha2r/robotiq3f_py/issues) in the repository.

![Ethernet Setup](https://github.com/baha2r/robotiq_3f_gripper/assets/75396051/2caa843d-18e1-429f-a00c-29b129244c32)
