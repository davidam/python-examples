import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 7227))

user_text = input("What do you want to send: ")
client_socket.send(user_text.encode())
answer = client_socket.recv(1024)
print("Server answer: ", answer.decode())
client_socket.close()