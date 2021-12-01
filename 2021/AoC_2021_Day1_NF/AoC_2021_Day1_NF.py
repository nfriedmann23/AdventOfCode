
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'AoC_2021_Day1_NF_input.txt'), 'r')



def part_one():
    counter = 0
    previous = 0
    for line in f:
        line = line.replace('\n', '')
        if int(line) > previous:
            counter = counter + 1
        previous = int(line)

    counter = counter-1
    print(counter)

def part_two():
    measurements = []
    for line in f:
        measurements.append(int(line))
    n = 0
    finals = []
    for i in measurements:
        try:
            measurements[n+2]
            if not n == 0:
                prevcacl = measurements[n-1] + measurements[n] + measurements[n+1]
            else: prevcacl = 0
            calc = measurements[n] + measurements[n+1] + measurements[n+2]
            if calc > prevcacl:
                updown = 'increased'
            else:
                updown = 'decreased'
            finals.append(str(calc) + ' ' + updown)
            n = n + 1
        except:
            pass
    print(finals)
    increases = -1
    for j in finals:
        if 'increased' in j:
            increases = increases + 1
    print(increases)


part_two()


    




