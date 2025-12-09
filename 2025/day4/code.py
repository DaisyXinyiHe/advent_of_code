import sys

# sys.stdin = open('./day4/test.txt', 'r')
sys.stdin = open('./day4/input.txt', 'r')
paper_grid = []
for i in sys.stdin:
    test_string = []
    element = i.strip()
    for e in element:
        test_string.append(e)
    paper_grid.append(test_string)
sys.stdin.close()


#### Part 1


def remove_process(paper_grid):
    fork_position = []
    total_fork = 0
    for r in range(len(paper_grid)):
        for c in range(len(paper_grid[0])):
            adj_paper_cnt = 0
            # print(r,c)
            if paper_grid[r][c] == '@':
                # count left rows
                
                if r == 0: ## count corner cases first
                    ## corner cases can always be mark as x because it will never have more than 4 rolls of paper in the 8 adj position
                    if c  == 0:
                        fork_position.append([r,c])
                        total_fork+=1
                    elif c == (len(paper_grid[0])-1):
                        fork_position.append([r,c])
                        total_fork+=1
                    else: ## If the paper is at the wall
                    # if c != 0  and c != (len(paper_grid[0])-1):
                        if paper_grid[r][c-1]=='@':
                            adj_paper_cnt +=1
                        if paper_grid[r][c+1]=='@':
                            adj_paper_cnt +=1
                        if paper_grid[r+1][c+1]=='@':
                            adj_paper_cnt +=1  
                        if paper_grid[r+1][c-1]=='@':
                            adj_paper_cnt +=1 
                        if paper_grid[r+1][c]=='@':
                            adj_paper_cnt +=1   
                        if adj_paper_cnt<4:
                            fork_position.append([r,c])
                            total_fork+=1
            
                        

                elif r == (len(paper_grid[0])-1):
                    if c  == 0:
                        fork_position.append([r,c])
                        total_fork+=1
                    elif c == (len(paper_grid[0])-1):
                        fork_position.append([r,c])
                        total_fork+=1 
                    else: ## If the paper is at the wall
                    # if c != 0  and c != (len(paper_grid[0])-1):
                        if paper_grid[r][c-1]=='@':
                            adj_paper_cnt +=1
                        if paper_grid[r][c+1]=='@':
                            adj_paper_cnt +=1
                        if paper_grid[r-1][c+1]=='@':
                            adj_paper_cnt +=1  
                        if paper_grid[r-1][c-1]=='@':
                            adj_paper_cnt +=1 
                        if paper_grid[r-1][c]=='@':
                            adj_paper_cnt +=1   
                        if adj_paper_cnt<4:
                            fork_position.append([r,c])
                            total_fork+=1                  
                else:
                    if c == 0:## If the paper is at the wall
                        if paper_grid[r][c+1]=='@':
                            adj_paper_cnt +=1
                        if paper_grid[r-1][c]=='@':
                            adj_paper_cnt +=1
                        if paper_grid[r-1][c+1]=='@':
                            adj_paper_cnt +=1  
                        if paper_grid[r+1][c]=='@':
                            adj_paper_cnt +=1 
                        if paper_grid[r+1][c+1]=='@':
                            adj_paper_cnt +=1  
                        if adj_paper_cnt<4:
                            fork_position.append([r,c])
                            total_fork+=1
                    elif c == (len(paper_grid[0])-1):## If the paper is at the wall
                        if paper_grid[r][c-1]=='@':
                            adj_paper_cnt +=1
                        if paper_grid[r-1][c]=='@':
                            adj_paper_cnt +=1
                        if paper_grid[r-1][c-1]=='@':
                            adj_paper_cnt +=1  
                        if paper_grid[r+1][c]=='@':
                            adj_paper_cnt +=1 
                        if paper_grid[r+1][c-1]=='@':
                            adj_paper_cnt +=1  
                        if adj_paper_cnt<4:
                            fork_position.append([r,c])
                            total_fork+=1
                    else: # if not in the corner or at the wall, check all places
                        if paper_grid[r][c-1]=='@':
                            adj_paper_cnt +=1
                        if paper_grid[r][c+1]=='@':
                            adj_paper_cnt +=1
                        if paper_grid[r-1][c]=='@':
                            adj_paper_cnt +=1  
                        if paper_grid[r-1][c+1]=='@':
                            adj_paper_cnt +=1 
                        if paper_grid[r-1][c-1]=='@':
                            adj_paper_cnt +=1  
                        if paper_grid[r+1][c]=='@':
                            adj_paper_cnt +=1  
                        if paper_grid[r+1][c+1]=='@':
                            adj_paper_cnt +=1 
                        if paper_grid[r+1][c-1]=='@':
                            adj_paper_cnt +=1 
                        if adj_paper_cnt<4:
                            fork_position.append([r,c])
                            total_fork+=1
                                                                

    print(total_fork)
    print(fork_position)

    return total_fork, fork_position



total_fork, fork_position = remove_process(paper_grid)
                    

## Part 2

## start:
for p in paper_grid:
    print(''.join(p))

total_fork, fork_position = remove_process(paper_grid)

## Loop until no more forking left
while len(fork_position) > 0: 

    for f in fork_position:
        paper_grid[f[0]][f[1]] = 'x'
    for p in paper_grid:
        print(''.join(p))   
    
    new_total_fork, fork_position = remove_process(paper_grid)
    print(fork_position)
    print(new_total_fork)

    total_fork+=new_total_fork

print(total_fork)


