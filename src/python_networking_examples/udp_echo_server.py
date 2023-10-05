import socket

# If you have nc installed, you can test this server by running:
# nc -vu localhost 65431
# Otherwise, you can use the client in src/python_networking_examples/udp_echo_client.py

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65431  # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 1024

def main():
    udp_socket_server()

def udp_socket_server():
    # Create a socket object using UDP as the transport protocol
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print(f"Binding to {HOST}:udp-{PORT}")
        # Bind the socket to the address and port
        s.bind((HOST, PORT))
        # Loop forever
        while True:
            # Receive data from the client
            bytes_address_pair = s.recvfrom(BUFFER_SIZE)
            # Print the received data to the server console
            message = bytes_address_pair[0]
            address = bytes_address_pair[1]
            message_str = str(message, encoding="utf-8")
            address_str = ":".join(str(x) for x in address)
            print(f"Message from Client: addr={address_str} message='{message_str}'")
            # Echo the data back to the client
            s.sendto(b'echo: ' + message, address)

if __name__ == "__main__":
    main()
