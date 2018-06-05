import socket
import os

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(('192.168.0.13',23333))

sock.send('')

sock.close()