import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# (ip, port)
server_socket.bind((socket.gethostname(), 7227))
server_socket.listen(20)

try:
    while True:
        close_connection = False
        print("Waiting connection ....")
        client_socket, client_address = server_socket.accept()
        print("Connection established: ", client_address)
        while not close_connection:
            try:
                message = client_socket.recv(1024)
                #.decode() -> bytes to str | .encode() -> str to  bytes
                print("Message received: ", message.decode())
                reply = "Welcome to the server"
                client_socket.send(reply.encode())
            except ConnectionAbortedError:
                print("Connection closed by the user")
                close_connection = True
except KeyboardInterrupt:
    print("Server closed by admin")

input()
