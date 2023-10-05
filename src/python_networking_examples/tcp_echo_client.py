import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
BUFFER_SIZE = 1024

def main():
    tcp_socket_client()

def tcp_socket_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")
        message = "Hello TCP server!"
        print(f"Sending message:  {message}")
        s.sendall(message.encode("utf-8"))
        data = s.recv(BUFFER_SIZE)

    print(f"Received message: {data.decode('utf-8')}")

if __name__ == "__main__":
    main()
