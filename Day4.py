with open('day4_input.txt', 'r') as f:
	data = f.read().strip().split('\n')

count = 0


for i in range(len(data)):
	line = data[i].split('-')
	number = line[-1].split('[')[0]
	match = line[-1].split('[')[1][:-1]

	for x in range(1 ,len(line) - 1):
		line[0] += line[x]

	print(line, number, match)

	lc = {}
	for letter in line[0]:
		lc[letter] = lc.get(letter, 0) + 1
	print(lc)

	occurences = []
	addsum = True

	for x in list(match):
		if x in lc:
			occurences.append(lc[x])
		else:
			addsum = False
			break;
	if addsum:
		if occurences == sorted(occurences, reverse = True):
			count += int(number)
	else:
		print('broken shit')

print(count)
#lc = sorted(lc, key = lc.get, reverse = True)[:6] #converts dict into list
#lc = ''.join(lc) #flattens list into string
#print(lc)


'''
1. Split data[0] by dashes
2. Concatenate the string peices
3. Split into chars and organize count
4. compare first five of char order to checksum
5. if good add ID to count
'''
