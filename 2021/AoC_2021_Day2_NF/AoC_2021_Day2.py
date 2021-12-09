import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'AoC_2021_Day2_NF_input.txt'), 'r')

def part_one():
	x = 0
	y = 0
	for line in f:
		line = line.replace('\n','')
		if "forward" in line:
			x = x + int(line.split(' ')[1])
		elif "down" in line:
			y = y + int(line.split(' ')[1])
		elif "up" in line:
			y = y - int(line.split(' ')[1])
	print(x)
	print(y)
	print(x*y)

def part_two():
	x = 0
	y = 0
	aim = 0
	for line in f:
		line = line.replace('\n','')
		if "forward" in line:
			if aim == 0:
				y = y
				x = x + int(line.split(' ')[1])
			else:
				y = y + (int(line.split(' ')[1]) * aim)
				x = x + int(line.split(' ')[1])
		elif "down" in line:
			aim = aim + int(line.split(' ')[1])
		else:
			aim = aim - int(line.split(' ')[1])
		print(line, x, y, aim)
	print(x*y)
	
	

part_two()