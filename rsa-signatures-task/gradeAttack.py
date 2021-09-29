from main import grade, sign
import requests
import json
import numpy as np
import math
import secrets

#Setup session with server
url = "http://127.0.0.1:5000/"
s = requests.Session()

def int_to_bytes(x: int) -> bytes: #Convert int to bytes
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')
    
def int_from_bytes(xbytes: bytes) -> int: #Convert bytes to int
    return int.from_bytes(xbytes, 'big')

def signMessage(message): #Send a string of hex chars to the server to sign
    resp1 = s.get(url+"sign_random_document_for_students/"+message)
    #print(resp1.text)
    resp = json.loads(resp1.text)
    #print(resp["msg"])
    #print(resp["signature"])
    return(resp["signature"])

def getPublicKey(): #Get the public key from the server
    resp1 = s.get(url+"pk/")
    resp = json.loads(resp1.text)
    return(resp["N"])
#________________________________________________________________________________    

#Get the public key
N = getPublicKey() #We need the public key for the modular inverse 

#The message that we want a signature for
maliciousMsg = "You got a 12 because you are an excellent student! :)".encode()

#Multiply the message with another known message k
k = secrets.token_bytes(math.ceil(N.bit_length() / 8)) #Create a random message with length N
malMsgK = (int.from_bytes(maliciousMsg, "big")*int.from_bytes(k, "big"))%N
malMsgK = malMsgK.to_bytes(math.ceil(N.bit_length() / 8), 'big')

#Send the 2 messages to the server to get the signatures
malSig = signMessage(str(malMsgK.hex()))
kSig = signMessage(str(k.hex()))

#Calculate the signature for the forbidden message from the 2 messages
malSigBytes = bytes.fromhex(malSig)
kSigBytes = bytes.fromhex(kSig)

#Get the signature for the forbidden message
gradeSig = ((int.from_bytes(malSigBytes, "big"))*pow((int.from_bytes(kSigBytes, "big")),-1,N))%N
gradeSig = gradeSig.to_bytes(math.ceil(N.bit_length() / 8), 'big').hex()
#Test against correct signature
print("Calculated signature: ", gradeSig)

realSig = signMessage(str("You got a 12 because you are an excellent student! :)").encode().hex()) #Removed rules from server to get this

print("realSig: ", realSig)

malMsgHex = int.from_bytes(maliciousMsg, "big")
malMsgHex = malMsgHex.to_bytes(math.ceil(N.bit_length() / 8), 'big')

cookie = {'msg':malMsgHex.hex(), 'signature':gradeSig}




#Get a quote using the message and signature
resp2 = s.get(url+"quote/",headers= {'Cookie':  'grade={}'.format(cookie)})

print(resp2.text)
resp = json.loads(resp2.text)


    