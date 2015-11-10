MAX_KEY_SIZE = 26

def getMode():
	print ("Do you want to encrypt, decrypt, or brute force a message (e, d, b)?")
	return raw_input()

def getMessage():
	print ("Enter your message:")
	return raw_input()

def getKey():
	print ("Enter the key number (1-%s)") % MAX_KEY_SIZE
	return raw_input()

def encrypt(message, key):
	char = ''
	result = ""
	for letter in message:
		char = ord(letter) + key
		result += chr(char)
	print ("Your translated text is: %s") % result

def decrypt(message, key):
	char = ''
	result = ""
	for letter in message:
		char = ord(letter) - key
		result += chr(char)
	print ("Your translated text is: %s") % result

def brute(message):
	for i in range(1, MAX_KEY_SIZE +1):
		decrypt(message, i)

mode = getMode()
if mode == 'e':
	message = getMessage()
	key = int(getKey())
	encrypt(message, key)
elif mode == 'd':
	message = getMessage()
	key = int(getKey())
	decrypt(message, key)
else:
	message = getMessage()	
	brute(message)
