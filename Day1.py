import csv

instructions = csv.reader(open('day1_input.txt', 'r'))
for item in instructions:
	item = ['' + item + '' for item in item]

inputs = item
inputs[0] = ' R3'

x = 0
y = 0

direction = 'N'

coordinates = [(0, 0)]

def chooseDirection(direction, move):
	if direction == 'N':
		North(move)
	elif direction == 'E':
		East(move)
	elif direction == 'S':
		South(move)
	elif direction == 'W':
		West(move)
	else:
		print('Incorrect Direction Entered')

def North(move):
	global x, direction, coordinates
	newMoves = []
	if move[0] == 'R':
		for new_x in range(x, x + int(move[1]), 1):
			coordinates.append((new_x + 1, y))
			newMoves.append((new_x + 1, y))
		x += int(move[1])
		print("Moved East", move[1], "units", newMoves)
		direction = 'E'
	else:
		for new_x in range(x, x - int(move[1]), -1):
			coordinates.append((new_x - 1, y))
			newMoves.append((new_x - 1, y))
		x -= int(move[1])
		print("Moved West", move[1], "units", newMoves)
		direction = 'W'
	
def East(move):
	global y, direction, coordinates
	newMoves = []
	if move[0] == 'R':
		for new_y in range(y, y - int(move[1]), -1):
			coordinates.append((x, new_y - 1))
			newMoves.append((x, new_y - 1))
		y -= int(move[1])
		print("Moved South", move[1], "units", newMoves)
		direction = 'S'
	else:
		for new_y in range(y, y + int(move[1]), 1):
			coordinates.append((x, new_y + 1))
			newMoves.append((x, new_y + 1))
		y += int(move[1])
		print("Moved North", move[1], "units", newMoves)
		direction = 'N'

def South(move):
	global x, direction, coordinates
	newMoves = []
	if move[0] == 'R':
		for new_x in range(x, x - int(move[1]), -1):
			coordinates.append((new_x - 1, y))
			newMoves.append((new_x - 1, y))
		x -= int(move[1])
		print("Moved West", move[1], "units", newMoves)
		direction = 'W'
	else:
		for new_x in range(x, x + int(move[1]), 1):
			coordinates.append((new_x + 1, y))
			newMoves.append((new_x + 1, y))
		x += int(move[1])
		print("Moved East", move[1], "units", newMoves)
		direction = 'E'

def West(move):
	global y, direction, coordinates
	newMoves = []
	if move[0] == 'R':
		for new_y in range(y, y + int(move[1]), 1):
			coordinates.append((x, new_y + 1))
			newMoves.append((x, new_y + 1))
		y += int(move[1])
		print("Moved North", move[1], "units", newMoves)
		direction = 'N'
	else:
		for new_y in range(y, y - int(move[1]), -1):
			coordinates.append((x, new_y - 1))
			newMoves.append((x, new_y - 1))
		y -= int(move[1])
		print("Moved South", move[1], "units", newMoves)
		direction = 'S'

for next_move in inputs:
	next_move = next_move[1:]
	next_move = next_move[0:1] + ' ' + next_move[1:]
	chooseDirection(direction, next_move.split())

print("x distance:", x)
print("y distance:", y)
print("Duplicate Location Found at:", [x for x in coordinates if coordinates.count(x) >= 2][0])