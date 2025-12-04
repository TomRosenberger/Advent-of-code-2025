with open("day4/input.txt") as file:
    grid = [[i for i in row.strip()] for row in file]

def get(grid,row,index):
    if row < 0 or row > len(grid) -1 or index < 0 or index > len(grid) -1:
        return 0
    else:
       roll = grid[row][index]
       if roll == "@":
           return 1
       else:
           return 0
    
output = 0
for row in range(len(grid)):
    for i in range(len(grid[0])):
        if grid[row][i] == ".":
            continue
        adjacent_rolls = 0
        for n in range(i-1,i+2):
            upper = get(grid,row-1,n)
            mid = get(grid,row,n)
            lower = get(grid,row+1,n)
            adjacent_rolls += upper + lower + mid
        if adjacent_rolls < 5:
            output +=1 
print(output)