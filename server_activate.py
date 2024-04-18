import socket
import threading
import json
from robotiq3f_py.robotiqcontrol.GripperController import GripperController  # Import your GripperController class

class GripperServer:
    def __init__(self, host='127.0.0.1', port=65432):
        self.gripper = GripperController("192.168.1.11")  # Example IP
        self.gripper.activate()  # Activate the gripper upon server start
        self.gripper.command_gripper(rPRA=[1, 1, 1], rSP=[250, 250, 250], rFR=[250, 250, 250], rMOD="Basic", rICF=False)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()
        print(f"Server listening on {host}:{port}")
    
    def handle_client(self, client_socket):
        with client_socket:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                # Deserialize the received JSON string back into Python data
                command = json.loads(data.decode('utf-8'))
                print(f"Received command: {command}")
                rPRA = [command[0]] * 3
                rSP = [command[1]] * 3
                rFR = [command[2]] * 3
                self.gripper.command_gripper(rPRA=rPRA, rSP=rSP, rFR=rFR)
                # Now command is a Python list that you can use
                
    def run(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connected by {addr}")
            thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            thread.start()

if __name__ == '__main__':
    server = GripperServer()
    server.run()
