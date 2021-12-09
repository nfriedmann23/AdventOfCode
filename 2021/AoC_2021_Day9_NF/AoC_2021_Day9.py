import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'AoC_2021_Day9_NF_input.txt'), 'r')


coordinates = []

for row in f:
	positions = []
	row = row.replace('\n','')
	for i in row:
		positions.append(int(i))
	coordinates.append(positions)

y = 0
x = 0
lowpoints = []

while y < 100:
	if y != 0 and y != 99:
		prevline = coordinates[y-1]
		line = coordinates[y]
		nextline = coordinates[y+1]
		x = 0
		while x < 100:
			if x!=0 and x != 99:
				checkup = prevline[x]
				checkback = line[x-1]
				checkforward = line[x+1]
				checkdown = nextline[x]
				print(line[x], checkup, checkback, checkforward, checkdown)
				if line[x] < min(checkup, checkback, checkforward, checkdown):
					print(line[x])
					lowpoints.append(line[x]+1)
				x = x + 1
			elif x == 0:
				checkup = prevline[x]
				checkforward = line[x+1]
				checkdown = nextline[x]
				print(line[x], checkup, checkforward, checkdown)
				if line[x] < min(checkup, checkforward, checkdown):
					print(line[x])
					lowpoints.append(line[x]+1)
				x = x + 1
			else:
				checkup = prevline[x]
				checkback = line[x-1]
				checkdown = nextline[x]
				print(line[x], checkup, checkback, checkdown)
				if line[x] < min(checkup, checkback, checkdown):
					print(line[x])
					lowpoints.append(line[x]+1)
				x = x + 1
		y = y + 1

	elif y == 0:
		line = coordinates[y]
		nextline = coordinates[y+1]
		x = 0
		while x < 100:
			if x!=0 and x != 99:
				checkback = line[x-1]
				checkforward = line[x+1]
				checkdown = nextline[x]
				print(line[x], checkback, checkforward, checkdown)
				if line[x] < min(checkback, checkforward, checkdown):
					print(line[x])
					lowpoints.append(line[x]+1)
				x = x + 1
			elif x == 0:
				checkforward = line[x+1]
				checkdown = nextline[x]
				print(line[x], checkforward, checkdown)
				if line[x] < min(checkforward, checkdown):
					print(line[x])
					lowpoints.append(line[x]+1)
				x = x + 1
			else:
				checkback = line[x-1]
				checkdown = nextline[x]
				print(line[x], checkback, checkdown)
				if line[x] < min(checkback, checkdown):
					print(line[x])
					lowpoints.append(line[x]+1)
				x = x + 1
		y = y+1

	elif y == 99:
		prevline = coordinates[y-1]
		line = coordinates[y]
		x = 0
		while x < 100:
			if x!=0 and x != 99:
				checkup = prevline[x]
				checkback = line[x-1]
				checkforward = line[x+1]
				if line[x] < min(checkup, checkback, checkforward):
					lowpoints.append(line[x]+1)
				x = x + 1
			elif x == 0:
				checkup = prevline[x]
				checkforward = line[x+1]
				if line[x] < min(checkup, checkforward):
					lowpoints.append(line[x]+1)
				x = x + 1
			else:
				checkup = prevline[x]
				checkback = line[x-1]
				if line[x] < min(checkup, checkback, checkdown):
					lowpoints.append(line[x]+1)
				x = x + 1
		y = y+1


print(sum(lowpoints))


	