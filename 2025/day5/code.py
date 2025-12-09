with open("./day5/test.txt", "r") as file:
# with open("./day5/input.txt", "r") as file:
    content = file.read().strip()

fresh_ing_ids, avail_ids = content.split("\n\n")  # split by empty line

fresh_ing_ids = fresh_ing_ids.splitlines()
avail_ids = list(map(int,avail_ids.splitlines()))


### extravagent test 
# fresh_ing_ids = ['12058563521803-1573920910374754537281','90987656789876545676543234567-91567656765678767876767867878987898789','0-4']
# avail_ids = [123456789876543,9876543456789,5,45676,6,3]

# print(fresh_ing_ids)
# print(avail_ids)

### Part 1

fresh_id_list = set()
for f in fresh_ing_ids:
    start = int(f.split('-')[0])
    end = int(f.split('-')[1])
    for a in avail_ids:
        if a >= start and a <= end:
            fresh_id_list.add(a)

print(len(fresh_id_list))
# print(fresh_id_list)


### Part 2

## It will be crazy to actually list count the number available

## Find overlapping merging range and calculate range

parsed = [tuple(map(int, f.split('-'))) for f in fresh_ing_ids ]
parsed.sort(key = lambda x:x[0])

merged = []
for start,end in parsed:
    if not merged or start > merged[-1][1]+1:
        merged.append([start,end])
    else:
        merged[-1][1] = max(merged[-1][1],end)

total_cnt_ids = 0
for m in merged:
    cnt = (m[1]-m[0])+1
    total_cnt_ids+=cnt

print(total_cnt_ids)





