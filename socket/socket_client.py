"""
客户端套接字，connect
"""
import socket

client = socket.socket()
client.connect(("127.0.0.1", 8080))
print(client.recv(1024))
print(client.recv(1024))
client.close()
