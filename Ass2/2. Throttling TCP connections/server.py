import socket

HOST = '192.168.43.112'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


while True:
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((HOST, PORT))
			s.settimeout(5)
			print("listening on "+str(HOST)+":"+str(PORT))
			s.listen()
			conn, addr = s.accept()
			with conn:
				print('Connected by', addr)
				while True:
					data = conn.recv(1024)
					print(data)
					if not data:
						break
					conn.sendall(data)
	except Exception as msg:
		print(msg)
