import socket

# This script is a simple TCP client that connects to a server, sends a message, and receives a response.

# Define the server address
ipaddress = "127.0.0.1"  # The IP address of the server to connect to.
port = 5004  # The port number of the server to connect to.

# Create a socket object
"""
AF_INET: Address Family-IPv4, AF_INET6: IPv6
    This means socket can connect to IPv4 addresses if AF_INET is used.
    If AF_INET6 is used, socket can connect to IPv6 addresses.

SOCK_STREAM: TCP, SOCK_DGRAM: UDP
    This means socket used Transport Layer-TCP if SOCK_STREAM is used.
    If SOCK_DGRAM is used, socket used TL-UDP.
"""
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a new socket using IPv4 and TCP.

# Connect to the server
socket.connect((ipaddress, port))  # Connect to the server at the specified IP address and port number.

# Create a message to send to the server
data_to_send = "Chaitanya"  # The message to send to the server.

# Convert string to bytes
data_in_bytes = bytes(data_to_send, "utf-8")  # Convert the message to bytes, using UTF-8 encoding.

# Send data to the server
socket.sendall(data_in_bytes)  # Send the message to the server.

# Receive data from the server and decode it
data_received = socket.recv(1024).decode("utf-8")  # Receive up to 1024 bytes from the server and decode it as a UTF-8 string.

# Print the data received from the server
print("Received data from the server: ", data_received)  # Print the message received from the server.

# Close the connection
socket.close()  # Close the connection to the server.