import socket
import threading
import os
import json

suma = ""


class ClientThread(threading.Thread):
    def __init__(self, client_socket, client_address):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address
        self.end = False

    def run(self):
        global suma
        print("Connection established: ", self.client_address)
        while not self.end:
            try:
                message = self.client_socket.recv(1024)
                # .decode() -> bytes to str | .encode() -> str to  bytes
                print("Message received: ", message.decode())
                msg_client = json.loads(message.decode())
                suma += msg_client["Message"] + "\n"
                reply = "Welcome to the server"
                self.client_socket.send(reply.encode())
            except ConnectionAbortedError:
                print("Connection closed by the user")
                self.end = True


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
            client_thread = ClientThread(client_socket, client_address)
            client_thread.start()



pid = os.getpid()
server_socket_thread = ServerSocketThread()
server_socket_thread.start()
input("Socket is listening. Press enter to exit")
print("Server closed by the admin.")
print(threading.active_count())
print("Total messages: ", suma)
os.kill(pid, -9)




