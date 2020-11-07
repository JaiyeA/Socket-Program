#Client

import socket
#1
client = socket.socket()
client.connect(('localhost',4000))
#2
user_name = input("Enter your name to connect: ")
client.send(bytes(user_name,"utf-8"))
#3
print(client.recv(2048).decode())
#4
connected = 1
while connected == 1:
    message = input("Compose a message or type 'exit' stop: ")
    if message.lower() == "exit":
        connected = 0
    client.send(bytes(message,"utf-8"))
