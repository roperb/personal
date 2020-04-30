#Project Euler Problem 15

def numPaths(x,y):
    grid = [ [0] * (y+1) for _ in range(x+1)]
    for i in range(y+1):
        grid[0][i]=1
    for j in range(x+1):
        grid[j][0]=1
    for i in range(1,x+1):
        for j in range(1,y+1):
            if grid[i][j] == 0:
                grid[i][j] = grid[i-1][j]+grid[i][j-1]
    print(grid[x][y])

numPaths(20,20)



"""
def numPaths(xpos,ypos,x,y):

    if xpos == x or ypos == y:
        return 1

    else:
        return numPaths(xpos+1,ypos,x,y)+numPaths(xpos,ypos+1,x,y)

print(numPaths(0,0,20,20))


    elif xpos == x and ypos < y:
        return numPaths(xpos,ypos+1,x,y)

    elif xpos < x and ypos == y:
        return numPaths(xpos+1,ypos,x,y)
    """