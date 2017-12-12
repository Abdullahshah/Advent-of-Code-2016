f = open('day2_input.txt', 'r')
codes = []
for line in f:
	codes.append(line)

x = 0
y = 0

noUp = [(0,0), (1,1), (2,2), (3,1), (4,0)]
noDown = [(0,0), (1,-1), (2,-2), (3,-1), (4,0)]
noRight = [(2, 2), (2,-2), (3, 1), (3, -1), (4, 0)]
noLeft = [(0,0), (2, 2), (2,-2), (1, 1), (1, -1)]

def up():
	global y
	if (x, y) not in noUp:
		y =+ 1 
	else:
		pass
def down():
	global y
	if (x, y) not in noDown:
		y -= 1
	else:
		pass
def right():
	global x
	if (x, y) not in noRight:
		x += 1
	else:
		pass
def left():
	global x
	if (x, y) not in noLeft:
		x -= 1
	else:
		pass

for line in codes:
	a = list(line)
	#del a[-1]
	for i in a:
		if i == 'U':
			up()
		elif i == 'D':
			down()
		elif i == 'R':
			right()
		elif i == 'L':
			left()
		else:
			pass
	print("Position:", x,",", y)