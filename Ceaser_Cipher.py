d={}
for i in range(0,26):
	d[i] = chr( i+65 )
for i in range(0,10):
	d[26+i] = chr(48+i)
	
d_inv = {}
for i in range(0,26):
	d_inv[chr( i+65 )] = i 
for i in range(0,10):
	d_inv[chr(48+i)] = 26+i

def encryption(pt, key):
	global d, d_inv
	ct = ''
	for char in pt:
		ct += d[(d_inv[char] + key) % 36]
	print("Cipher Text : ",ct)
	return ct

def decryption(ct, key):
	global d, d_inv
	pt =''
	
	for char in ct:
		pt += d[(d_inv[char] - key) % 36]
	
	print("Plain Text: ",pt)

def bruteForce(ct):
	key = range(0,36)
	pt = []
	temp = ''
	for k in key:
		for char in ct:			
			temp += d[(d_inv[char] - k) % 36]
		
		pt.append(temp)
		temp = ''
		
	print("-------PLAIN TEXT CAN BE ANY ONE OF FOLLOWING-------")
	for i in range(0,36):
		print(i+1,pt[i])
		
	
pt1 = raw_input("Enter the Plain Text: ")

key1 = int(raw_input('enter the Key: '))

ct1 = encryption(pt1, key1)

decryption(ct1, key1)

bruteForce(ct1)

