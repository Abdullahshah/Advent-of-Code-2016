with open('day3_input.txt', 'r') as f:
	data = f.read().strip().split("\n")

colA = []
colB = []
colC = []

for x in range(len(data)):
	data[x] = data[x].split()
	colA.append(int(data[x][0]))
	colB.append(int(data[x][1]))
	colC.append(int(data[x][2]))

colA = [colA[i:i + 3] for i in range(0, len(colA), 3)]
colB = [colB[i:i + 3] for i in range(0, len(colB), 3)]
colC = [colC[i:i + 3] for i in range(0, len(colC), 3)]

def getTriangles(numbers):
	count = 0
	for x in numbers:
		one = x[0] + x[1] > x[2]
		two = x[1] + x[2] > x[0]
		three = x[0] + x[2] > x[1]
		if one and two and three:
			count += 1
		else:
			pass
	print(count)

getTriangles(colA)
getTriangles(colB)
getTriangles(colC)