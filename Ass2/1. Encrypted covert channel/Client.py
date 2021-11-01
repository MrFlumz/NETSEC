from icmplib import ping
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode
from Crypto.Util.Padding import pad

data = b"Test message!!!" #The message we Want to send through the covert channel
#key = get_random_bytes(16)
key = b'\xe5\xa5L\xab\xd1hU=G\x08\xc8\xa2\xd8R\xcc\xa9' #Pre-shared symmetric key

# Encrypt the payload message using AES with CBC encoding
cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(data, AES.block_size))

iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ciphertext).decode('utf-8')

# We combine the encrypted message with the iv, so the message can be decrypted
pl = iv + ct

# Send an ICMP package with the payload, using icmplib's ping function.
host = ping('127.0.0.1', count=5000, interval=0.2, payload = pl.encode())

