
import socket

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((socket.gethostname(), 8000))
# become a server socket
serversocket.listen(5000)
print(socket.gethostname())
print(serversocket.listen(5000))
