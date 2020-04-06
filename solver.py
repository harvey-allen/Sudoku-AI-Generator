import numpy as np
import random

#Defining the variables
soloutions = 0
originalGrid = [[4, 5, 8, 7, 3, 9, 6, 1, 2],
[2, 6, 9, 4, 5, 1, 3, 8, 7],
[7, 3, 1, 2, 6, 8, 5, 9, 4],
[5, 9, 2, 3, 1, 4, 8, 7, 6],
[3, 1, 4, 6, 8, 7, 9, 2, 5],
[6, 8, 7, 5, 9, 2, 1, 4, 3],
[8, 4, 3, 9, 7, 6, 2, 5, 1],
[1, 2, 5, 8, 4, 3, 7, 6, 9],
[9, 7, 6, 1, 2, 5, 4, 3, 8]]

### Generating ###
def shuffle(grid):
    if random.choice([True, False]): #Swap Rows
        tempRow1 = random.randint(0, 8)
        if 0 <= tempRow1 < 3: #Ensures the swap occurs in the same block
            tempRow2 = random.randint(0, 2)
        elif 3 <= tempRow1 < 6:
            tempRow2 = random.randint(3, 5)
        else:
            tempRow2 = random.randint(6, 8)
        if tempRow1 != tempRow2: #Performing the swap
            tempRow = grid[tempRow1]
            grid[tempRow1] = grid[tempRow2]
            grid[tempRow2] = tempRow
    else: #Swap Columns
        tempColumn1 = random.randint(0, 8)
        if 0 <= tempColumn1 < 3: #Ensures the swap occurs in the same block
            tempColumn2 = random.randint(0, 2)
        elif 3 <= tempColumn1 < 6:
            tempColumn2 = random.randint(3, 5)
        else:
            tempColumn2 = random.randint(6, 8)
        if tempColumn1 != tempColumn2:
            for row in range(9): #Performing the swap
                tempColumn = grid[row][tempColumn1]
                grid[row][tempColumn1] = grid[row][tempColumn2]
                grid[row][tempColumn2] = tempColumn
    return grid
                    
def pairRemoval(grid):
    randX = random.randint(0, 8)
    randY = random.randint(0, 8)
    grid[randY][randX] = 0
    grid[8 - randY][8 - randX] = 0 #Rotational Counterpart
    return grid
    
    
### Solving ###
def possible(y, x, n, grid):
    for i in range(0, 9): #Column Check
        if grid[y][i] == n:
            return False
    for i in range(0, 9): #Row Check
        if grid[i][x] == n:
            return False
    xSquare = (x//3)*3
    ySquare = (y//3)*3
    for i in range(0, 3): #Square Check
        for j in range(0, 3):
            if grid[ySquare+i][xSquare+j] == n:
                return False
    return True
    
def solver(grid): #Recursive Function
    global soloutions
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n, grid): #Backtracking
                        grid[y][x] = n
                        solver(grid)
                        grid[y][x] = 0
                return
    soloutions += 1


### Main Process ###
def main(grid):
    originalGrid = grid
    print("Searching...")
    while soloutions == 0: #Generates potential grids until a solvable one is found
        for i in range(random.randint(10, 1000)):
            grid = shuffle(originalGrid)
        for i in range(random.randint(15, 20)):
            grid = pairRemoval(originalGrid)
        finalProduct = grid
        solver(grid)
    print("Genrated Grid:")
    print(np.matrix(finalProduct))
    print("")
    blanks = 0
    for y in range(9): #Calculating the number of blank spaces
        for x in range(9):
            if grid[y][x] == 0:
                blanks += 1
    print("Number of blanks: " + str(blanks))
    print("")
    print("Soloutions: " + str(soloutions))
    if soloutions == 1: #Calculating the difficulty
        print("Difficulty: Hard")
    elif 1 < soloutions <= 5:
        print("Difficulty: Medium")
    else:
        print("Difficulty: Easy")
    
    
main(originalGrid)


