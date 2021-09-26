import requests

# splits string into a list of chunk sized strings
# split_str(['123456'],2) = ['12','34','56']
def split_str(seq, chunk, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(split_str(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst

#url = "https://cbc.syssec.lnrd.net/"
url = "http://127.0.0.1:5000/"

s = requests.Session()
resp1 = s.get(url)
#print(resp1.headers)
auth = resp1.cookies.get('authtoken')
blocks = split_str(auth, 32) #splits string into a list of 32 char sized strings
plaintext = [0]*16
finalstring = ""

for part in range(int(len(auth)/32)-1):
	guess_block = ''.join(blocks[0+part:1+part])
	guess_block = split_str(guess_block, 2)  #splits string into a list of 2 char sized strings
	cifertext = ''.join(blocks[1+part:2+part])
	plaintext = [0]*16

	for char in range(16):

		for i in range(256):
			# guessblock 
			gb = guess_block.copy()

			# guess all values after current guess value		
			for u in range(char):
				gb[15-u] = (plaintext[15-u] ^ int(gb[15-u],16)) ^ (char+1)
				gb[15-u] = hex(gb[15-u])[2:].zfill(2)

			# foremost guess in guessblock
			gb[15-char] = int(gb[15-char],16) ^ i ^ (char + 1)
			gb[15-char] = hex(gb[15-char])[2:].zfill(2)# zfill zero pads ahead of hex so 1 > 01

			
			newauth = ''.join(gb)+''.join(cifertext)
			rest2 = s.get(url+ "quote/",headers= {'Cookie':  'authtoken={}'.format(newauth)})
			string = str(rest2.content, 'utf-8')
			if string == "No quote for you!":
				plaintext[15-char] = i
				#print(''.join([chr(ch) for ch in plaintext]))
				#break # <-- this breaks the final block for some reason ???????

	# save plaintext
	finalstring += ''.join([chr(ch) for ch in plaintext])
	print(finalstring)
			
			
		
		
		