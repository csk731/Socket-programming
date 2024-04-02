import socket

# This script is a simple TCP server that listens for incoming connections, receives a message, sends a response, and then closes the connection.

# Define the server address
ipaddress = "127.0.0.1"  # The IP address of the server to bind to.
port = 5004  # The port number of the server to bind to.

# Create a socket object
"""
AF_INET: Address Family-IPv4, AF_INET6: IPv6
    This means socket can bind to IPv4 addresses if AF_INET is used.
    If AF_INET6 is used, socket can bind to IPv6 addresses.

SOCK_STREAM: TCP, SOCK_DGRAM: UDP
    This means socket used Transport Layer-TCP if SOCK_STREAM is used.
    If SOCK_DGRAM is used, socket used TL-UDP.
"""
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a new socket using IPv4 and TCP.

# Bind the socket to the server address
socket.bind((ipaddress, port))  # Bind the socket to the specified IP address and port number.

# Listen for incoming connections
socket.listen()  # Start listening for incoming connections.

# Communication loop with the client
while True:
    """
    This is the main loop of the server. It continuously accepts incoming connections, receives a message, sends a response, and then closes the connection.
    """
    # Accept the connection
    client_socket, client_address = socket.accept()  # Accept an incoming connection and get the client socket and address.

    # Receive data from the client and decode it
    data_received = client_socket.recv(1024).decode("utf-8")  # Receive up to 1024 bytes from the client and decode it as a UTF-8 string.

    # Print the data received from the client
    print("Received data from the client: ", data_received)  # Print the message received from the client.

    # Create a message to send to the client
    data = "Hello, " + data_received + "!"  # The message to send to the client.

    # Convert string to bytes
    data_in_bytes = bytes(data, "utf-8")  # Convert the message to bytes, using UTF-8 encoding.

    # Send data to the client
    client_socket.sendall(data_in_bytes)  # Send the message to the client.

    # Close the connection
    client_socket.close()  # Close the connection to the client.