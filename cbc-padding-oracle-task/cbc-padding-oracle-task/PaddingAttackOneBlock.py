

import httplib2
import json
import requests
import numpy as np

url = "https://cbc.syssec.lnrd.net/"
url = "http://127.0.0.1:5000/"

def split_str(seq, chunk, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(split_str(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst



s = requests.Session()
resp1 = s.get(url)
#print(resp1.headers)
auth = resp1.cookies.get('authtoken')

print('auth: '+str(auth))
blocks = split_str(auth, 32)
print(blocks)
print('block 0: ' +str(blocks[0]))
#print('block last byte: ' +str(blocks[0][15]))

iv_blocks = ''.join(blocks[0:1])
print(iv_blocks)
cifertext = ''.join(blocks[1:2])

print("cifer " + cifertext)
finalstring = ""
originalIV = split_str(iv_blocks, 2)
for blocknr in range(5):
	print(block)
	print(blocknr)
	plaintext = [0]*16
	for char in range(16):
		#print("char" + str(char))
		for i in range(256):
			#print(i)
			bfblock = split_str(block, 2)
			#print(bfblock)
			# guess all IV values after current IV value		
			for u in range(char):
				bfblock[15-u] = (plaintext[15-u] ^ int(bfblock[15-u],16)) ^ (char+1)
				bfblock[15-u] = hex(bfblock[15-u])[2:].zfill(2)

			
			# current IV guess
			bfblock[15-char] = int(bfblock[15-char],16) ^ i ^ (char + 1)
			bfblock[15-char] = hex(bfblock[15-char])[2:].zfill(2)# zfill zero pads ahead of hex so 1 > 01
			#print(bfblock)
			#print(blocknr)
			#print(cifertext)
			#print("block ''.join(blocks[:i])"+ ''.join(blocks[:blocknr]))
			#print("block ''.join(blocks[i+1:]"+ ''.join(blocks[blocknr+1:blocknr+2]))
			#print('auth    : '+str(auth))
			newauth = ''.join(bfblock)+''.join(blocks[blocknr+1:blocknr+2])

			#print("newauth : "+newauth)
			rest2 = s.get( url + "quote/",headers= {'Cookie':  'authtoken={}'.format(newauth)})
			string = str(rest2.content, 'utf-8')
			#print(string)
			if string == "No quote for you!":
				plaintext[15-char] = i
				#print(chr(i))
				print(''.join([chr(ch) for ch in plaintext]))
				#print("newauth : "+newauth)
				#print('auth    : '+str(auth))
				break
				#print(iv)
				continue
			#elif string == "Padding is incorrect." or string == "PKCS#7 padding is incorrect.":
			#	continue
			else:
				#print(string)
				continue
			#print(plaintext)
	finalstring += ''.join([chr(ch) for ch in plaintext])
	print(finalstring)
	if blocknr > 1:
		break
	#input(">>")	
		
	
			
		
		
		
		
		
#print(iv)
#newauth = ''.join(iv)+''.join(cifertext)
#rest2 = s.get(url + "quote/",headers= {'Cookie':  'authtoken={}'.format(newauth)})
#string = str(rest2.content, 'utf-8')	
#print(string)
	#str(resp1.headers['set-cookie']).replace("authtoken=",'')



#blocks[7] = "0000000011111111"
#blocks[7]

	
#response, content  = httplib2.Http().request("http://localhost:5000",'GET')

#headers = {'set-cookie': str(response['set-cookie'])} # .replace("authtoken=",'')

#cookies = {'authtoken': response['set-cookie']}
#print("header: "+str(response))
#resp, content = httplib2.Http().request("http://localhost:5000/quote/", headers=cookies)
#print("content: "+str(content))
