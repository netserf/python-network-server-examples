import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65431  # The port used by the server
BUFFER_SIZE = 1024

def main():
    udp_socket_client()

def udp_socket_client():
    # Create a socket object using UDP as the transport protocol
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Send to server using created UDP socket
    message = "Hello UDP server!"
    print(f"Sending message:  {message}")
    s.sendto(message.encode('utf-8'), (HOST, PORT))
    print(f"Datagram sent to {HOST}:{PORT}")
    bytes_address_pair = s.recvfrom(BUFFER_SIZE)
    response = str(bytes_address_pair[0], encoding="utf-8")
    print(f"Received response: {response}")

if __name__ == "__main__":
    main()
