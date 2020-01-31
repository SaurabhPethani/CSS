import textwrap as text

print("Sap Id: 60004188011")
print("-----Welcome To Columnar Cipher---")
PT = input("Enter the Plain Text: ")
key = input("Enter the Key: ")

keyLen = len(key)
ptLen = len(PT)
dummy = keyLen - (ptLen % keyLen)
if dummy < 6:
	for i in range(dummy):
		PT += chr(95)
dummyKey = key
ptLen = len(PT)
no_of_rows = ptLen // keyLen

#Creating Matrix
mat = text.wrap(PT, keyLen)
priKey = sorted(key)
CT = ''
for i in range(keyLen):
	pri = priKey[i]
	ind = dummyKey.find(pri)

	for j in range(no_of_rows):
		CT += mat[j][ind]

	for l in range(len(dummyKey)):
		if dummyKey[l] == pri:
			dummyKey = dummyKey[:l]+'x'+dummyKey[l+1:]
			break
print("Cipher Text: ", CT)
CTList = text.wrap(CT, no_of_rows)
newPT = []

for x in range(len(priKey)):
	newPT.append('x')

dummyKey = key

for i in range(len(priKey)):
	val = CTList[i]	
	index = dummyKey.find(priKey[i])

	newPT[index] = val
	for l in range(len(dummyKey)):
		if dummyKey[l] == priKey[i]:
			dummyKey = dummyKey[:l]+'x'+dummyKey[l+1:]
			break
no_of_rows = ptLen // keyLen
print("SAP ID: 60004188011")
print("Decryption")
print("Cipher Text : ",CT)
print("Plain Text (From CT): ",end='')
for i in range(no_of_rows):
	for j in range(len(newPT)):
		print(newPT[j][i], end='')

