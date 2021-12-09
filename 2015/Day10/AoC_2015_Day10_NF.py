
from itertools import permutations


puzzleinput = '3113322113'
startpostition = 0
combostring = ''
iterstring = ''
i = 0

while i < 50:
    # combostring = puzzleinput[startpostition]
    spos = 0

    for n in puzzleinput:
        combostring = ''
        count = 1
        multistring = ''
        if startpostition+1 < len(puzzleinput):
            combostring = puzzleinput[startpostition]
            while puzzleinput[startpostition] == puzzleinput[startpostition+1]:
                multistring = str(1+ count) + puzzleinput[startpostition+1]
                startpostition = startpostition + 1
                count = count + 1
        if len(multistring) > 0:
            iterstring = iterstring + multistring
            startpostition = startpostition + 1
        elif len(puzzleinput) == startpostition +1:
            combostring = puzzleinput[startpostition]
            iterstring = iterstring + str(len(combostring)) + combostring
            startpostition = startpostition + 1
        else:
            iterstring = iterstring + str(len(combostring)) + combostring
            startpostition = startpostition + 1
        spos = spos + 1
        # print(iterstring.replace('0',''))
    # iterstring = iterstring + str(len(combostring)) + puzzleinput[startpostition-1]
    puzzleinput = iterstring.replace('0','')
    startpostition = 0
    iterstring = ''
    i = i+1
    print(i)

print(len(puzzleinput))
    
        

    
    
