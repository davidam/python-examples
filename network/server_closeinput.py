import socket
import threading
import os

class ServerSocketThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop = False
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((socket.gethostname(), 7227))
        self.server_socket.listen(20)

    def run(self):
        while True:
            close_connection = False
            print("Waiting connection ....")
            client_socket, client_address = self.server_socket.accept()
            print("Connection established: ", client_address)
            while not close_connection:
                try:
                    message = client_socket.recv(1024)
                    # .decode() -> bytes to str | .encode() -> str to  bytes
                    print("Message received: ", message.decode())
                    reply = "Welcome to the server"
                    client_socket.send(reply.encode())
                except ConnectionAbortedError:
                    print("Connection closed by the user")
                    close_connection = True


pid = os.getpid()
server_socket_thread = ServerSocketThread()
server_socket_thread.start()
input("Socket is listening. Press enter to exit")
print("Server closed by the admin.")
os.kill(pid, -9)
