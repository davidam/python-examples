import socket
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 7227))
exit = False
while not exit:
    user_text = input("What do you want to send: ")
    if user_text == "exit":
        exit = True
    else:
        message = {"Message": user_text}
        client_socket.send(json.dumps(message).encode())
        answer = client_socket.recv(1024)
        print("Server answer: ", answer.decode())
client_socket.close()
