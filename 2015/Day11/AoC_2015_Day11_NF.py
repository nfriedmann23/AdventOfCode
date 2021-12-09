
from itertools import groupby


# puzzleinput = 'hxbxwxba'
puzzleinput = 'hxbxxzaa'

def new_password_gen(last_pass):

    def condition1(input):
        cond1 = False if any(substring in ['i','o','l'] for substring in input) else True
        return cond1
    
    def condition2(input):
        numdups = sum(len(list(dups)) >= 2 for _, dups in groupby(input))
        cond2 = False
        if numdups >= 2:
            cond2 = True
        return cond2

    def condition3(input):
        for i in range(len(input)-2):
            first = input[i]
            second = input[i+1]
            third = input[i+2]
            cond1a = first == chr(ord(second)-1)
            cond1b = second == chr(ord(third)-1)
            cond3 = cond1a and cond1b is True
            if cond3 is True: break
        return cond3


        # startstring = 'abc'
        # cond3 = False
        # while startstring != 'xyz':
        #     if startstring in input:
        #         cond3 = True
        #         break
        #     else:
        #         startstring = ''.join(chr(ord(letter)+1) for letter in startstring)

        # return cond3


    while last_pass[1] != 'z':
        if (condition1(last_pass) and condition2(last_pass) and condition3(last_pass)) is True:
            break
        if last_pass[-1] != 'z':
            last_pass =  last_pass[:-1] + last_pass[-1].replace(last_pass[-1],(chr(ord(last_pass[-1])+1)))
            print(last_pass)
        
        if last_pass[-1] == 'z':
            i = 1
            while i < len(last_pass):
                if (condition1(last_pass) and condition2(last_pass) and condition3(last_pass)) is True:
                    break
                elif last_pass[-i] == 'z':
                    i = i+1
                    print(last_pass)
                else:
                    last_pass =  last_pass[:-i] + last_pass[-i].replace(last_pass[-i],(chr(ord(last_pass[-i])+1))) + ((i-1) * 'a')
                    print(last_pass)
                    break
        
    print(f'answer is {last_pass}')
    return last_pass


new_password_gen(puzzleinput)
