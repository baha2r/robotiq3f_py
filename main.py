from GripperController import GripperController
import time

# Initialize the GripperController object by specifying the server IP
gripper = GripperController("192.168.1.11")

# Activate the gripper
gripper.activate()

# Define command parameters
target_position = [200, 20, 11]
speed = [25, 205, 250]
force = [25, 250, 250]

mode = "Basic" # Gripper mode. Other options: "Basic", "Wide", "Pinch", "Scissor"
individual_control = True # If False, only the first element of target_position, speed, and force is used
target_position = [target_position[0]] * 3 if not individual_control else target_position
    
# Send the command to the gripper
gripper.command_gripper(rPRA=target_position, rSP=speed, rFR=force, rMOD=mode, rICF=individual_control)

# Wait until the target position is achieved
while ([gripper.FingerA_Position, gripper.FingerB_Position, gripper.FingerC_Position] != target_position):
    time.sleep(0.1)

# Print the positions of the fingers
print(f"FingerA_Position: {gripper.FingerA_Position} FingerB_Position: {gripper.FingerB_Position} FingerC_Position: {gripper.FingerC_Position}")

# send new command
individual_control = False
target_position = [150, 20, 110]
mode = "Basic"
target_position = [target_position[0]] * 3 if not individual_control else target_position
gripper.command_gripper(rPRA=target_position, rSP=speed, rFR=force, rMOD=mode, rICF=individual_control)
while ([gripper.FingerA_Position, gripper.FingerB_Position, gripper.FingerC_Position] != target_position):
    time.sleep(0.1)
print(f"FingerA_Position: {gripper.FingerA_Position} FingerB_Position: {gripper.FingerB_Position} FingerC_Position: {gripper.FingerC_Position}")

# Close the connection when done
gripper.close()

