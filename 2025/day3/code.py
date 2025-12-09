

import sys

sys.stdin = open('./day3/input.txt', 'r')
test = []
for i in sys.stdin:
    element = i.strip()
    test.append(element)
sys.stdin.close()


### Part 1

# test = [
# '987654321111111',
# '811111111111119',
# '234234234234278',
# '818181911112111',
# '81818193111111',

# ]

# total_jolt = 0

# for joltage in test:
#     ## 2 pointers method

#     p1 = 0
#     p2 = len(joltage)-1
#     curr_max = int(joltage[p1]+joltage[p2])
#     p1_max = 0
#     p2_max = len(joltage)-1

#     # print('start:',curr_max)

#     while p1<(len(joltage)-1):

#         if int(joltage[p1]+joltage[p2])>curr_max:
#             curr_max = int(joltage[p1]+joltage[p2])
#             p1_max = p1
        
#         p1+=1
    
#     while p2>(p1_max):
        
#         # print(p2)
#         if int(joltage[p1_max]+joltage[p2])>curr_max:
#             curr_max = int(joltage[p1_max]+joltage[p2])
#             p2_max = p2
#         p2-=1
    

#     total_jolt+=curr_max
#     # print(joltage,' :',curr_max)
# print(total_jolt)
        
##### Part 2

# test = [
# '987654321111111',
# '811111111111119',
# '234234234234278',
# '818181911112111',
# # '81818193111111',

# ]

total_sum = 0
for jolt in test:

    max_seq_len = 12
    p_start_max = len(jolt) - max_seq_len
    p_end_max = max_seq_len
    # print(jolt[:p_end_max], jolt[p_start_max:len(jolt)])

    ## Save digit position in position dictionary
    position_dict = {}
    for i in range(len(jolt)):
        position_dict[i] = jolt[i]

    # print(position_dict)

    ## select start point
    p1 = 0
    p1_val = jolt[p1]
    for k,v in position_dict.items():
        if k <= p_start_max:
            if p1_val < v:
                p1_val = v
                p1 = k
    
    # print('start point:',p1,p1_val, jolt[p1:(p1+max_seq_len)])

    # curr_max =  jolt[p1:(p1+max_seq_len)]
    

    if p1 == p_start_max:
        num =  jolt[p1:(p1+max_seq_len)]
    else:
        num = jolt[p1]
        p_next = p1+1
        p_next_val = jolt[p_next]
        max_seq_len-=1
        p_next_max = (len(jolt) - max_seq_len)
        
        while p_next < p_next_max and max_seq_len>0:
            
            

            # for k,v in position_dict.items():
            for k in range(p_next,p_next_max+1):
                # print(k,position_dict[k])
                if int(p_next_val) < int(position_dict[k]):
                    # print(p_next,k,position_dict[k])
                    p_next = k
                    p_next_val = position_dict[k]
                    # break
                else:
                    p_next_val = position_dict[p_next]
                    # print(p_next,position_dict[p_next])
            num+=p_next_val
            p_next+=1
            max_seq_len-=1
            
            p_next_max = (len(jolt) - max_seq_len)
            # print(p_next, p_next_max,num, jolt[p_next:(p_next+max_seq_len)],max_seq_len)
        
        # print(num)
        
        if len(num)< 12:
            num+=jolt[p_next:(p_next+max_seq_len)]

        print(num)
    total_sum+=int(num)

print(total_sum)













    