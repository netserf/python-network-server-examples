import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65431  # The port used by the server
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Send to server using created UDP socket
s.sendto(b"Hello UDP server!", (HOST, PORT))
bytes_address_pair = s.recvfrom(BUFFER_SIZE)
message = str(bytes_address_pair[0], encoding="utf-8")
address = ":".join(str(x) for x in bytes_address_pair[1])
print(f"Message from Server: addr={address} message='{message}'")
