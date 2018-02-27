import hashlib
import time

def hashpasskey(index):
	index = index
	count = 0
	password = ''
	while count < 8:
		hash_object = hashlib.md5(('ugkcyxxp' + str(index)).encode())
		hash_string = hash_object.hexdigest()
		if hash_string[:5] != '00000':
			index += 1
		else:
			print(hash_string[5:6], str(index))
			index += 1
			count += 1
			password += hash_string[5:6]
	return password
	
if __name__ == '__main__':
	index = 0
	start = time.time()
	print("Password: " + hashpasskey(index))
	end = time.time()
	print("time:" + str(end - start))