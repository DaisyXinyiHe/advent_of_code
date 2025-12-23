
puzzle = []
# with open("./day7/test.txt", "r") as file:
# with open("./day7/test2.txt", "r") as file:
with open("./day7/input.txt", "r") as file:
    new_line = []
    for line in file:
        line = line.replace('\n','')
        puzzle.append(list(line))

## Part 1
# total = 0
# for row in range(len(puzzle)):
#     for col in range(len(puzzle[0])):
#         # print(puzzle[row][col])
#         if puzzle[row][col] == 'S':
#             puzzle[row+1][col] = '|'
#             print(puzzle[row+1][col])
#         if puzzle[row][col] == '|':
#             if puzzle[row+1][col] == '^':
#                 if col == 0:
#                     puzzle[row+1][col+1] = '|'
#                 elif col == len(puzzle[0])-1:
#                     puzzle[row+1][col-1] = '|'
#                 else:
#                     puzzle[row+1][col-1] = '|'
#                     puzzle[row+1][col+1] = '|'
#                 total+=1
#             elif puzzle[row+1][col] == '.':
#                 puzzle[row+1][col] = '|'




# for r in puzzle:
#     print(r)
# print(total)


### Part 2
### Find on reddit: https://www.reddit.com/r/adventofcode/comments/1pg9w66/2025_day_7_solutions/
### Visual explanation: https://www.reddit.com/r/adventofcode/comments/1pgbg8a/2025_day_7_part_2_visualization_for_the_sample/
beams = [0]* len(puzzle[0])
beams[''.join(puzzle[0]).find("S")] = 1
for p in puzzle[2::2]:
    line = ''.join(p)
    pos = -1
    while (pos:=line.find("^",pos+1))!=-1:
        if(count:= beams[pos]):
            beams[pos] = 0
            beams[pos-1] +=count
            beams[pos+1] +=count

print(sum(beams))

