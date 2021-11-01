import socket
import time
import datetime
HOST = '192.168.43.112'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
import os

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    i = 6
    
    randomstring = str(os.urandom(128))
    #time.sleep(5)
    # we time 5000 transmissions
    time1 = time.time()
    for transmissions in range(100000):
        st = 'Hello, world :'+str(i) #+ randomstring
        s.sendall(st.encode("utf-8"))
        data = s.recv(1024).decode("utf-8") 
        print('Received', repr(data))
        time.sleep(0.05)
        i += 1

    time2 = time.time()
    print(time2-time1)