
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

for part in range( int(len(auth)/32)-1):
	guess_block = ''.join(blocks[0+part:1+part])
	guess_block = split_str(guess_block, 2)  #splits string into a list of 2 char sized strings
	cifertext = ''.join(blocks[1+part:2+part])
	plaintext = [0]*16

	# iterator for within he blocks
	for block_i in range(16):

		# checks all chars 0 - 256
		for char in range(0, 256):
			# guessblock 
			# This is the IV for the first iteration, and then the previous ciferblocks for the next iterations
			gb = guess_block.copy()

			# xor all the values in block, and add padding correspondingly
			for u in range(block_i): 
				gb[15-u] = (plaintext[15-u] ^ int(gb[15-u],16)) ^ (block_i+1)
				gb[15-u] = hex(gb[15-u])[2:].zfill(2)

			# foremost guess in guessblock
			gb[15-block_i] = int(gb[15-block_i],16) ^ char ^ (block_i + 1)
			gb[15-block_i] = hex(gb[15-block_i])[2:].zfill(2)# zfill zero pads ahead of hex so 1 > 01

			
			newauth = ''.join(gb)+''.join(cifertext)
			# set cookie
			rest2 = s.get(url+ "quote/",headers= {'Cookie':  'authtoken={}'.format(newauth)})
			string = str(rest2.content, 'utf-8')

			# this string is only returned if the message was padded correcly.
			if string == "No quote for you!":
				
				plaintext[15-block_i] = char
				print("i is " + chr(char)+ " " +str(char))
				print(''.join([chr(ch) for ch in plaintext]))
				if char>31: # if the found char is not a special operator
					break	
				

	# save plaintext
	finalstring += ''.join([chr(ch) for ch in plaintext])
	print(finalstring)
			
			
		
		
		