math_problem = []
with open("./day6/test.txt", "r") as file:
# with open("./day6/input.txt", "r") as file:
    for line in file:
        element = line.strip().split()
        math_problem.append(element)


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
operations = math_problem[len(math_problem)-1]
math_matrix = math_problem[:-1]

t_math_matrix =[]

for c in range(len(math_matrix[0])):
    new_row = []
    for r in range(len(math_matrix)):
        new_row.append(math_matrix[r][c])
    t_math_matrix.append(new_row)

print(t_math_matrix)


