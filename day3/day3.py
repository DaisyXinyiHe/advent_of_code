import os
os.getcwd()

## Part one
with open('input.txt') as f:
    lines = f.read().splitlines() 


def get_sum(lines):
    total_sum = 0
    for i in range(len(lines)):
        items = lines[i]
        shared = set(items[0:int(len(items)/2)])&set(items[int(len(items)/2):len(items)])
        # print(list(shared)[0])
        if ord(list(shared)[0])>=97:
            ## For lower case, set digit to 1~26
            # print(ord(list(shared)[0]) - 96)
            total_sum += ord(list(shared)[0]) - 96
        else:
            # print(ord(list(shared)[0])-64+26)
            ## For upper case, set digit to 27~52
            total_sum += ord(list(shared)[0])-64+26
            
    return total_sum

print('part one:', get_sum(lines))

## Part two

def get_badge_sum(lines):
    total_sum=0
    i=0
    while i < len(lines):
        group = lines[i:i+3]
        # print(group)
        shared = set(group[0])&set(group[1])&set(group[2])
        # print(shared)
        if ord(list(shared)[0])>=97:
            ## For lower case, set digit to 1~26
            total_sum+=ord(list(shared)[0]) - 96
        else:
        ## For upper case, set digit to 27~52
            total_sum+=ord(list(shared)[0])-64+26
        i+=3
    return total_sum

print('part two:',get_badge_sum(lines))


