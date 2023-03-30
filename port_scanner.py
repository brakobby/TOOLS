import socket

# Define a function to generate a range of ports to scan
def generate_port_range(start_port, end_port):
    return range(start_port, end_port + 1)

# Get the IP address of the target machine
target = input("Enter target IP address: ")

# Generate a range of ports to scan
start_port = int(input("Enter starting port number: "))
end_port = int(input("Enter ending port number: "))
port_range = generate_port_range(start_port, end_port)

# Loop through the range of ports and scan each one
for port in port_range:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target, port))

    if result == 0:
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))

    sock.close()