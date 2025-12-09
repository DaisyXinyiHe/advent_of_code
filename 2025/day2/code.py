import sys
# test = ['11-22',	
#         '95-115',
# '998-1012',	'1188511880-1188511890',	'222220-222224',
# '1698522-1698528',	'446443-446449',	'38593856-38593862',	'565653-565659',	
# '824824821-824824827',	'2121212118-2121212124'
# ]

sys.stdin = open('./day2/input.txt', 'r')
test = []
for i in sys.stdin:
    test = i.strip().split(',')
sys.stdin.close()


### Part 1
total_sum = 0
for t in test:
    id_range_start = t.split('-')[0]
    id_range_end = t.split('-')[1]

    if id_range_start[0] == '0':
        id_range_start=id_range_start[1:]
    if id_range_end[0] == '0':
        id_range_end = id_range_end[1:]


    ## Range of odd number of digits will not have repeated twiced sequences
    print(id_range_start ,len(id_range_start))
    print(id_range_end ,len(id_range_end))

    search_range = [int(id_range_start), int(id_range_end)]

    ## Find search range
    for i in range(len(id_range_start),len(id_range_end)+1, 1):
        next_100 = 10**i
        if next_100 > int(id_range_start) and next_100 < int(id_range_end):
            search_range.append(next_100)
    
    print(sorted(search_range))
    search_range=sorted(search_range)


    ## Range of odd number of digits will not have repeated twiced sequences
    for i in range(len(search_range)-1):
        # print(search_range[i], search_range[i+1])
        if len(str(search_range[i]))%2>0: ## Range of odd number of digits will not have repeated twiced sequences
            pass
        else:
            if len(str(search_range[i+1]))%2>0:
                search_id = [str(x) for x in range(search_range[i], search_range[i+1],1)]
            else:
                search_id = [str(x) for x in range(search_range[i], search_range[i+1]+1,1)]
            # print(search_id)
            for id in search_id:
                if id[:int(len(id)/2)] == id[int(len(id)/2):]:
                    total_sum+=int(id)
                    # print(id)



print('part 1:',total_sum)


## Part 2

## 1st method (sub-optimal)

total_sum = 0
invalid_id2 = set()
for t in test:
    id_range_start = t.split('-')[0]
    id_range_end = t.split('-')[1]

    if id_range_start[0] == '0':
        id_range_start=id_range_start[1:]
    if id_range_end[0] == '0':
        id_range_end = id_range_end[1:]
    
    search_range = [int(id_range_start), int(id_range_end)]
    # print(search_range)

    ## Find search range

    # search_range = [x for x in range(int(id_range_start),int(id_range_end)+1,len(id_range_start)*10)]+[int(id_range_start), int(id_range_end)]
    search_range  =  [x for x in range(int(id_range_start), int(id_range_end) + 1) if x % 10 == 0]+[int(id_range_start), int(id_range_end)]
    search_range=sorted(list(set(search_range)))
    # print(search_range)
    avail_num=[]

    for i in range(len(search_range)-1):
        # print(search_range[i], search_range[i+1])
        curr_search_range = [str(search_range[i]), str(search_range[i+1])]
        # curr_search_start = str(curr_search_range[0])
        # print(curr_search_range)
        pattern = []

        for num in curr_search_range:
            # print(num)
            curr_search_start = num
            for d in range(len(curr_search_start)+1):
                if curr_search_start[:d] != '':
                    p = curr_search_start[:d]
                    # print(p)
                    pattern.append(p)
                    check_num = [p*x for x in range(2,len(curr_search_start)+1) if len(p*x)<=len(curr_search_range[1])]
                    # print(check_num)
                    for c in check_num:
                        if int(c)>=int(curr_search_range[0]) and int(c)<=int(curr_search_range[1]):
                            if c not in avail_num:
                                avail_num.append(c)
                                invalid_id2.add(int(c))
        
        # print(pattern)
        # print(avail_num) 
        # for p in pattern:
        #     if p!='':

        #         check_num = p*len(curr_search_start)
        #         print(check_num)
        #         if int(check_num)>=int(curr_search_range[0]) and int(check_num)<=int(curr_search_range[1]):
        #             avail_num.append(check_num)
    # print(avail_num)

    for num in avail_num:
        total_sum+=int(num)

# print(avail_num)
print('part2:',total_sum)
# print(invalid_id2)



      
### 2nd method: More optimal method (got from the internet)
invalid_id = set()
for t in test:
    id_range_start = int(t.split('-')[0])
    id_range_end = int(t.split('-')[1])

    for total_len in range(2,len(str(id_range_end))+2):
        for p_len in range(1,total_len//2+1):
            if total_len%p_len!=0: continue
            min_p = 10**(p_len-1)
            max_p = 10**p_len-1
            for p in range(min_p, max_p+1):
                num=int(str(p)*(total_len // p_len))
                if id_range_start <= num <= id_range_end:
                    invalid_id.add(num)
print('part2 (optimal):',sum(invalid_id))