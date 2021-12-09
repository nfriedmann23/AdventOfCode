import json
import pandas as pd
import ast
import os
from itertools import chain

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
# f = os.path.join(__location__, 'Nathan_Input.json')
f = open(os.path.join(__location__, 'Nathan_Input.json'), 'r')

# df = json.load(f)
# df = str(df)
# df = df.replace(":","")
# df = df.replace("{","")
# df = df.replace("}","")
# df = df.replace("[","")
# df = df.replace("]","")
# df = df.replace( ",","'")
# df = df.replace(' ', '')
# df = df.split("'")
# print(df)
# input()
# sum = 0
# for i in df:
#     try:
#         if int(i):
#             sum = sum + int(i)
#         else:
#             pass
#     except:
#         print(i)

# print(sum)

df = json.load(f)


def object_type(input):
    listcount = 0
    dictcount = 0
    listdict = {"ListNum":[], "ListValues":[]}
    dictdict = {"DictNum":[],"DictValues":[]}
    for i in df:
        print(type(i))
        if type(i) == list:
            listdict["ListNum"].append(listcount)
            listdict["ListValues"].append(i)
            listcount = listcount + 1
            # object_type(i)
            df.remove(i)
        elif dict(i):
            dictdict["DictNum"].append(dictcount)
            dictdict["DictValues"].append(i)
            dictcount = dictcount + 1
            df.remove(i)
    return listdict, dictdict
    
L, D = object_type(df)
print(L)
print(D)

    