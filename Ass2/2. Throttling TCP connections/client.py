import socket
import time
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    i = 6
    while True:
        st = 'Hello, world :'+str(i)
        s.sendall(st.encode("utf-8"))
        data = s.recv(1024).decode("utf-8") 
        print('Received', repr(data))
        time.sleep(1)
        i += 1
