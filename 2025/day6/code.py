# import re
# math_problem = []
# # with open("./day6/test.txt", "r") as file:
# # with open("./day6/test2.txt", "r") as file:
# # with open("./day6/input.txt", "r") as file:
#     for line in file:
#         print(line)
#         element = line.strip().split()

#         math_problem.append(element)


#### Part 1
# operations = math_problem[len(math_problem)-1]

# math_matrix = math_problem[:-1]

# total_final = 0
# for c in range(len(math_matrix[0])):
#     for r in range(len(math_matrix)):
#         num = int(math_matrix[r][c])
#         if operations[c] == '*':
#             if r  == 0:
#                 final = num
#             else:
#                 final*=num
#         elif operations[c] == '+':
#             if r  == 0:
#                 final = num
#             else:
#                 final+=num
#         elif operations[c] == '-':
#             if r  == 0:
#                 final = num
#             else:
#                 final-=num
#         elif operations[c] == '/':
#             if r  == 0:
#                 final = num
#             else:
#                 final/=num
            
#     total_final+=final
# print(total_final)

# ## Maybe could even use numpy transpose to spolve this. Can try later. 

### Part 2

import re
math_problem = []
# with open("./day6/test.txt", "r") as file:
# with open("./day6/test2.txt", "r") as file:
with open("./day6/input.txt", "r") as file:
    new_line = []
    for line in file:
        line = line.replace('\n','')
        math_problem.append(line)
  

operations = math_problem[len(math_problem)-1]
operations = operations.strip().split(' ')
operations = [o for o in operations if o !='']




math_matrix = math_problem[:-1]


op=0
# while op <=len(operations):
#     row = math_matrix[op]

new_row = []
for c in range(len(math_matrix[0])):
    newnum = ''

    # for r in range(len(math_matrix)):

    for r in range(len(math_matrix)):
        # new_row.append(math_matrix[r][c].replace(' ','*'))
        newnum += math_matrix[r][c].replace(' ','*')
        print(newnum)

    # if newnum == len(newnum)* '*':
    #     t_math_matrix.append(new_row)
    #     new_row = []
    # else:
    
    new_row.append(newnum)

t_math_matrix =[]
new_row2 = []
for r in new_row:
    if r == len(r)*'*':
        # print(new_row2)

        t_math_matrix.append(new_row2)
        new_row2=[]
    else:
        new_row2.append(r)
if new_row2:
    t_math_matrix.append(new_row2)


grand_total = 0
for op in range(len(operations)):
    row = t_math_matrix[op]
    if operations[op] == '*':
        result = 1
        for r in row:
            result*=int(r.replace('*',''))
    elif operations[op] == '+':
        result = 0
        for r in row:
            result+=int(r.replace('*',''))
    grand_total+=result


print(grand_total)