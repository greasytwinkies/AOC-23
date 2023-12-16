import sys
sys.setrecursionlimit(100000)

with open("input.txt", "r") as f:
    file = f.read()

# convert into 2d array
lines = file.split('\n')
grid = [[x for x in line] for line in lines]

for line in grid:
    print(line)
print()

# things to take note of
# 1. direction of beam travel
# 2. orientation of mirror
# 3. grid boundaries

global edict
edict = dict()
def reset_edict(grid):    
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            edict[x,y] = list()
            # each entry in the dictionary will contain a list of directions of rays coming in
    
def check_boundary(grid, row, column, direction):
    if direction == "U" and row == 0:
        return True
    elif direction == "D" and row == len(grid)-1:
        return True
    elif direction == "R" and column == len(grid[0])-1:
        return True
    elif direction == "L" and column == 0:
        return True
    else:
        return False # not at boundary, continue as per normal


def traversal(grid, row, column, direction):
    # out of bounds
    if row < 0 or row >= len(grid) or column < 0 or column >= len(grid):
       return # check entry in energy dict
    if direction in edict[row, column]:
        return #looping
    else:
        edict[row, column].append(direction)
        # check type of space/mirror
        tile = grid[row][column]
        if tile == ".": # continue in the same direction
            if direction == "U":
                traversal(grid, row-1, column, direction)
            elif direction == "D":
                traversal(grid, row+1, column, direction)
            elif direction == "L":
                traversal(grid, row, column-1, direction)
            elif direction == "R":
                traversal(grid, row, column+1, direction)
        elif tile == "/":
            if direction == "U": # deflects to the right
                traversal(grid, row, column+1, "R")
            elif direction == "D": # deflects to the left
                traversal(grid, row, column-1, "L")
            elif direction == "L": # deflects down 
                traversal(grid, row+1, column, "D")
            elif direction == "R": # deflects up
                traversal(grid, row-1, column, "U")
        elif tile == "\\":
            if direction == "U": # deflects to the left
                traversal(grid, row, column-1, "L")
            elif direction == "D": # deflects to the right
                traversal(grid, row, column+1, "R")
            elif direction == "L": # deflects up
                traversal(grid, row-1, column, "U")
            elif direction == "R": # deflects down
                traversal(grid, row+1, column, "D")
        elif tile == "|":
            if direction == "U": # just continues up
                traversal(grid, row-1, column, direction)
            elif direction == "D": # just continues down
                traversal(grid, row+1, column, direction)
            elif direction == "L" or direction == "R": # deflects up and down
                traversal(grid, row-1, column, "U")
                traversal(grid, row+1, column, "D")
        elif tile == "-":
            if direction == "L": # just continues left
                traversal(grid, row, column-1, direction)
            elif direction == "R": # just continues right
                traversal(grid, row, column+1, direction)
            elif direction == "U" or direction == "D": # deflects left and right
                traversal(grid, row, column-1, "L")
                traversal(grid, row, column+1, "R")

def check_max(grid, r, c, direction):
    reset_edict(grid)
    traversal(grid, r, c, direction)
    egrid = [["." for x in line] for line in grid]
    for k in edict.keys():
        r, c = k
        if edict[k]:
            egrid[r][c] = "#"
    local_max = sum([line.count("#") for line in egrid])
    return local_max

max_energy = 0
for n in range(len(grid[0])): # first row
    local_max = check_max(grid, 0, n, "D")
    max_energy = local_max if local_max > max_energy else max_energy
    local_max = check_max(grid, len(grid), n, "U")
    max_energy = local_max if local_max > max_energy else max_energy

for n in range(len(grid)): # first column
    local_max = check_max(grid, n, 0, "R")
    max_energy = local_max if local_max > max_energy else max_energy
    local_max = check_max(grid, n, len(grid[0])-1, "L")
    max_energy = local_max if local_max > max_energy else max_energy

print(f"Number of energized tiles in most optimal configuration: {max_energy}")


