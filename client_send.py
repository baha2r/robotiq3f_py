import socket
import json
import time

def send_command(command, host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        json_command = json.dumps(command)
        s.sendall(json_command.encode('utf-8'))
        print(f"Sent command: {json_command}")


if __name__ == '__main__':
    # send_command([20, 200, 200])
    # Example command
    for i in range(10,200,10):
        command = [150, 50, i]
        send_command(command)
        time.sleep(1)

