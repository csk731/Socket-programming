import socket
import threading

# Define the server address
ipaddress = "127.0.0.1"
port = 5004

# Create a socket object
"""
AF_INET: Address Family-IPv4, AF_INET6: IPv6
    This means socket can connect to IPv4 addresses if AF_INET is used.
    If AF_INET6 is used, socket can connect to IPv6 addresses.

SOCK_STREAM: TCP, SOCK_DGRAM: UDP
    This means socket used Transport Layer-TCP if SOCK_STREAM is used.
    If SOCK_DGRAM is used, socket used TL-UDP.
"""
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
socket.bind((ipaddress, port))

# Listen for incoming connections
socket.listen()


def handle_connection(connection, client_address):
    # Receive data from the client and decode it
    data_received = connection.recv(1024).decode("utf-8")

    # Print the data received from the client
    print("Received data from the client: ", data_received)

    # Create a message to send to the client
    data = "Hello, " + data_received + "!"

    # Convert string to bytes
    data_in_bytes = bytes(data, "utf-8")

    # Send data to the client
    connection.sendall(data_in_bytes)

    # Close the connection
    connection.close()


while True:
    # Accept the connection and handle it
    client_socket, client_address = socket.accept()
    thread = threading.Thread(target=handle_connection, args=(client_socket, client_address))
    thread.start()


