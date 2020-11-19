import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# (ip, port)
server_socket.bind((socket.gethostname(), 7227))
server_socket.listen(20)

print("Waiting connection ....")
client_socket, client_address = server_socket.accept()
print("Connection established: ", client_address)
message = client_socket.recv(1024)
#.decode() -> bytes to str | .encode() -> str to  bytes
print("Message received: ", message.decode())
reply = "Welcome to the server"
client_socket.send(reply.encode())

client_socket.close()
server_socket.close()
