import os
import numpy as np
import itertools

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')
# f = open(r'C:\Users\natha\Documents\PyLibrary\NathanAdventofCode\2015\Day8\input.txt', 'r')
# esc = html.unescape(mem)


def part_one():
    places = []
    distanceslist = []
    for line in f:
        line = line.replace('to ', '')
        line = line.replace('= ', '')
        line = line.replace('\n', '')
        origin, destination, distance = line.split(' ')
        origintuple = tuple(line.split(' '))
        a, b, c = origintuple
        newtuple = b,a,c
        distanceslist.append(newtuple)
        distanceslist.append(tuple(line.split(' ')))
        places.append(origin)
        places.append(destination)
    locations = list(set(places))
    possibilities = list(itertools.permutations(locations))
    startmin = 0
    for p in possibilities:
        start = 0
        p = list(p)
        plen = 0
        print(p)
        while len(p) > plen+1:
            print(p[plen])
            print(p[plen+1])
            dist = [z for x, y, z in distanceslist if x == p[plen] and y == p[plen+1]]
            print(dist)
            if dist == []:
                start = 0
                plen = len(p)
            elif len(dist) == 1:
                start = start + int(dist[0])
            plen = plen + 1
        if startmin == 0:
            startmin = start
        elif start < startmin:
            startmin = start
        print(startmin)
        # if startmin != 0:
        #     input('waiting')
    return startmin

print(part_one())
