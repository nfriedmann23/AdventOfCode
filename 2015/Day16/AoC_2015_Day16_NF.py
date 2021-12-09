import os
from numpy.lib.utils import source
import pandas as pd
import numpy as np

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'AoC_2015_Day16_NF.txt'), 'r')


source_dict = {"children":int(3),
               "cats":int(7),
               "samoyeds":int(2),
               "pomeranians":int(3),
               "akitas":int(0),
               "vizslas":int(0),
               "goldfish":int(5),
               "trees":int(3),
               "cars":int(2),
               "perfumes":int(1)}

data_dict = {}
for line in f:
    line = line.replace('\n','')
    line1 = line.replace(',','')
    linelist = line1.split(':')
    line2 = line.split(":", 1)[1]
    line2 = line2.replace(' ', '')
    line2 = line2.replace("'", '')
    line2 = line2.split(',')
    data_dict[linelist[0]] = {
                    line2[0].split(':')[0]:int(line2[0].split(':')[1]),
                    line2[1].split(':')[0]:int(line2[1].split(':')[1]),
                    line2[2].split(':')[0]:int(line2[2].split(':')[1])}

true_list = []
for key, value in data_dict.items():
    true_count = 0
    print(key)
    print(value)
    print(value[0])
    print(int(value[0][1]))
    if (value[0][0], int(value[0][1])) in source_dict.items():
        true_count += 1
    if (value[1][0], int(value[1][1])) in source_dict.items():
        true_count += 1
    if (value[2][0], int(value[2][1])) in source_dict.items():
        true_count += 1
    if true_count == 3:
        true_list.append(key)

print(true_list)