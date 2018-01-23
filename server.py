import socket

clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clisock.connect(('10.14.113.160', 23000))

message = "Hello how are you?"

clisock.send(message.encode('utf-8'))

#clisock.send(bytes("Hello World\n"))

print(clisock. recv(100))

clisock.close()
