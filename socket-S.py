#Server
import socket
#1
server = socket.socket()
server.bind(('localhost',4000))
print("listening on localhost port 4000")
server.listen(2)
#2
print("Waiting for a connection")
c, address = server.accept()
name = c.recv(2048).decode()
print("Connected with",name,"at",address)
greeting = "Hello "+name+"!"
c.send(bytes(greeting,"utf-8"))
#3
while True:
    client_message = c.recv(2048).decode()
    if client_message != "":
        print(name+": "+client_message)

c.close()
