import socket
from Crypto.Cipher import AES
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


key = b'\xe5\xa5L\xab\xd1hU=G\x08\xc8\xa2\xd8R\xcc\xa9' #Pre-shared symmetric key
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
while True:
	with socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP) as s:
		s.bind((HOST, PORT))
		data, addr = s.recvfrom(1508)
		#print(data[28:])
		payload = data[28:]
		iv = payload[:24]
		iv = b64decode(iv)
		ct = payload[24:]
		ct = b64decode(ct)

		cipher = AES.new(key, AES.MODE_CBC, iv)
		pt = unpad(cipher.decrypt(ct), AES.block_size)
		print("The message was: ", pt)