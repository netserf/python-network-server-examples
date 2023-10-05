import socket

# If you have nc installed, you can test this server by running:
# nc -v localhost 65432
# Otherwise, you can use the client in src/python_networking_examples/tcp_echo_client.py

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 1024

def main():
    tcp_socket_server()

def tcp_socket_server():
    # Create a socket object using TCP as the transport protocol
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Binding to {HOST}:{PORT} (tcp)")
        # Bind the socket to the address and port
        s.bind((HOST, PORT))
        s.listen()
        # Block execution and wait for a connection
        conn, addr = s.accept()
        addr_str = ":".join(str(x) for x in addr)
        with conn:
            # Print message to the server console
            print(f"Client connection from {addr_str}")
            # Loop forever
            while True:
                # Receive data from the client
                data = conn.recv(BUFFER_SIZE)
                # Print the received data to the server console
                print(f"Received message: {data.decode('utf-8')}")
                # If no data is received, break out of the loop
                if not data:
                    break
                # Echo the data back to the client
                response = f"echo ... {data.decode('utf-8')}"
                print(f"Sending response:  {response}")
                conn.sendall(response.encode("utf-8"))

if __name__ == "__main__":
    main()
