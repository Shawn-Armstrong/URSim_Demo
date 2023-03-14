import sys
import socket
import logging

HOST_IP_ADDRESS = socket.gethostbyname(socket.gethostname())
PORT = 30002
command = "movej([0, 0, 0, 0, 0, 0], a=1.0, v=1.0)\n"
# command2 = "get_controller_temp()\n" # Not used.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.settimeout(4)

    print("Connecting with {}:{}".format(HOST_IP_ADDRESS, PORT))
    try:
        client_socket.connect((HOST_IP_ADDRESS, PORT))
    except socket.timeout as e:
        logging.error("Timeout error: {}".format(e))
        sys.exit(1)
    except socket.error as e:
        logging.error("Could not connect to {}:{} Error: {}".format(HOST_IP_ADDRESS, PORT, e))
        sys.exit(1)
    try:
        print("Sending command {} to UR3e simulator.".format(command[:-1]))
        client_socket.sendall(command.encode())
    except socket.error as e:
        logging.error("Sendall failed. Error: {}".format(e))
        sys.exit(1)

    response = client_socket.recv(4096)

if response:
    print(f"\nClient received: {response!r}")
    client_socket.close()
    sys.exit(0)
else:
    logging.error("No response message received.")
    client_socket.close()
    sys.exit(1)
