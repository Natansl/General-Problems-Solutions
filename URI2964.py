N, M, C = input().split()
maxRow = int(N)
maxCol = int(M)
grid = [[0 for col in range(maxCol)] for row in range(maxRow)]
nextGrid = [[0 for col in range(maxCol)] for row in range(maxRow)]

intact = int(C)
inGrid = intact 

for car in range(int(C)):
    line, col, direct = input().split()
    grid[int(line)-1][int(col)-1] = direct
while inGrid > 0:
    for i in range(maxRow):
        for j in range(maxCol):
            val = grid[i][j]
            if val == 0:
                continue
            incLine = 0
            incCol = 0
            if val == 'N':
                incLine = -1
            elif val == 'S':
                incLine = 1
            elif val == 'O':
                incCol = -1
            elif val == 'L':
                incCol = 1
            if (i + incLine < 0 or i + incLine == maxRow) or (j + incCol < 0 or j + incCol == maxCol):
                inGrid -= 1
            else:
                if (incLine == 1 and grid[i+incLine][j] == 'N'):
                    nextGrid[i][j] = val + grid[i+incLine][j]
                    grid[i][j] = 0
                    grid[i+incLine][j] = 0
                    intact -= 2
                    inGrid -= 2
                elif (incLine == -1 and grid[i+incLine][j] == 'S'):
                    nextGrid[i+incLine][j] = val + grid[i+incLine][j]
                    grid[i][j] = 0
                    grid[i+incLine][j] = 0
                    intact -= 2
                    inGrid -= 2
                elif(incCol == 1 and grid[i][j+incCol] == 'O'):
                    nextGrid[i][j+incCol] = val + grid[i][j+incCol]
                    grid[i][j] = 0
                    grid[i+incCol][j] = 0
                    intact -= 2
                    inGrid -= 2 
                elif(incCol == -1 and grid[i][j+incCol] == 'L'):
                    nextGrid[i][j] = val + grid[i][j+incCol]
                    grid[i][j] = 0
                    grid[i][j+incCol] = 0
                    intact -= 2
                    inGrid -= 2 
                else:
                    if nextGrid[i+incLine][j+incCol] != 0:
                        if len(nextGrid[i+incLine][j+incCol]) == 1:
                            intact -= 1
                            inGrid -= 1
                        intact -= 1
                        inGrid -= 1
                    if nextGrid[i+incLine][j+incCol] == 0:
                        nextGrid[i+incLine][j+incCol] = val
                    else:    
                        nextGrid[i+incLine][j+incCol] += val
    grid = nextGrid
    nextGrid = [[0 for col in range(maxCol)] for row in range(maxRow)]
print(intact)
