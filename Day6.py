from collections import Counter
with open('day6_input.txt', 'r') as f:
	data = f.read().strip().split("\n")

#	print(len(data[0]))
code = ''
for i in range(len(data[0])):
	columns = []
	for x in data:
		columns.append(x[i])
	count = Counter(columns)
	code += count.most_common()[-1][0]
print(code)