import socket
import threading

# Define the server address
ipaddress = "127.0.0.1"
port = 5004


def connect_to_server(number):
    """
    AF_INET: Address Family-IPv4, AF_INET6: IPv6
        This means socket can connect to IPv4 addresses if AF_INET is used.
        If AF_INET6 is used, socket can connect to IPv6 addresses.
    
    SOCK_STREAM: TCP, SOCK_DGRAM: UDP
        This means socket used Transport Layer-TCP if SOCK_STREAM is used.
        If SOCK_DGRAM is used, socket used TL-UDP.
    """
    # Create a socket object
    socket_created = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    socket_created.connect((ipaddress, port))

    # Create a message to send to the server
    data_to_send = "Chaitanya : " + number

    # Convert string to bytes
    data_in_bytes = bytes(data_to_send, "utf-8")

    # Send data to the server
    socket_created.sendall(data_in_bytes)

    # Receive data from the server and decode it
    data_received = socket_created.recv(1024).decode("utf-8")

    # Print the data received from the server
    print("Received data from the server: ", data_received)

    # Close the connection
    socket_created.close()


for i in range(10):
    thread = threading.Thread(target=connect_to_server, args=(str(i)))
    thread.start()