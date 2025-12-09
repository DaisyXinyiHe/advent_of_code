import sys

list_num = [x for x in range(0,100,1)]
start_point = 50
start_num = list_num[start_point]
zero_count = 0
total_zero_pass = 0

# def dial_code(i, start_point):
#     prev_point = start_point
#     zero_pass = 0
#     if i[0] == 'L':
#         start_point-=int(i[1:])
#         zero_pass += abs(start_point//100)
#         if start_point<-100:
#             start_point = start_point % 100
#     elif i[0] == 'R':
#         start_point+=int(i[1:])
#         zero_pass += abs(start_point//100)
#         if prev_point<0 and start_point>0:
#             zero_pass +=1
#         if start_point>=100:
#             start_point = start_point % 100
#     # print(start_point,abs(start_point//100))
#     return start_point,zero_pass

########### Decode #####################
# Open the text file in read mode
# sys.stdin = open('./day1/test.txt', 'r')
sys.stdin = open('./day1/input.txt', 'r')
# Now, any calls to input() or sys.stdin.readline() will read from 'input.txt'


list_num = [x for x in range(0,100,1)]
start_point = 50
start_num = list_num[start_point]
zero_count = 0
total_zero_pass = 0

zero_pass = 0
for direction in sys.stdin:
    i = direction.strip()

    
    print(i)


    zero_pass = 0
    if i[0] == 'L':

        ## Calculate zero pass
        if start_point==0:
            zero_pass = int(i[1:])//100
        elif int(i[1:])>= start_point:
            zero_pass = (int(i[1:]) - start_point) // 100+1
        else:
            zero_pass =0
        
        ## Calculate at 0 times
        start_point-=int(i[1:])
        if start_point<-100:
            start_point = start_point % 100


    elif i[0] == 'R':


        ## Calculate zero pass
        zero_pass =(start_point+int(i[1:]))//100
        start_point+=int(i[1:])

        # calculate at 0 times
        if start_point>=100:
            start_point = start_point % 100
    

    start_num = list_num[start_point]
    start_point = start_num
    if start_num == 0:
        zero_count+=1
    total_zero_pass+=zero_pass
    print(f"Direction:{i} point:{str(start_point)} Curr_code: {str(start_num)}")

    ## Remove double count in zero 
    print(f"zero counts: {zero_count}, zero_pass:{str(total_zero_pass)}")


# Close the file (optional, as it will be closed when the script ends)
# sys.stdin.close()


