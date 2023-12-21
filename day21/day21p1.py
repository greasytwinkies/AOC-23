import sys
from functools import cache
sys.setrecursionlimit(1000000)

with open("input.txt", "r") as f:
    file = f.read()

lines = file.split('\n')

global grid; grid = [[x for x in line] for line in lines]

# find coord of S
for index, line in enumerate(grid):
    if "S" in line:
        start = (index, line.index("S"))

# 16 steps: 0, 2, 4, 6, 8, 10, 12, 14, 16
# only care about the new steps
        
def check_valid(r, c):
    if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid)) or grid[r][c] == "#":
        return False
    return True
    
def move_dir(r, c, moves, direction):
    if direction == 0:
        if check_valid(r-1, c):
            if check_valid(r-2, c):
                moves.add((r-2, c))
            if check_valid(r-1, c-1):
                moves.add((r-1, c-1))
            if check_valid(r-1, c+1):
                moves.add((r-1, c+1))
    elif direction == 1:
        if check_valid(r+1, c):
            if check_valid(r+2, c):
                moves.add((r+2, c))
            if check_valid(r+1, c-1):
                moves.add((r+1, c-1))
            if check_valid(r+1, c+1):
                moves.add((r+1, c+1))
    elif direction == 2:
        if check_valid(r, c-1):
            if check_valid(r, c-2):
                moves.add((r, c-2))
            if check_valid(r-1, c-1):
                moves.add((r-1, c-1))
            if check_valid(r+1, c-1):
                moves.add((r+1, c-1))
    elif direction == 3:
        if check_valid(r, c+1):
            if check_valid(r, c+2):
                moves.add((r, c+2))
            if check_valid(r-1, c+1):
                moves.add((r-1, c+1))
            if check_valid(r+1, c+1):
                moves.add((r+1, c+1))
    return moves

@cache
def get_poss_moves(current, steps, target):
    # skips one move in between
    if steps == target:
        return
    r, c = current
    moves = set()
    for i in range(4):
        moves = move_dir(r, c, moves, i)
    for move in moves:
        get_poss_moves(move, steps+2, target)
    # update grid based on moves
    for r, c in moves:
        grid[r][c] = "O"

get_poss_moves(start, 0, 20)

count = 0

for line in grid:
    count = count + line.count("O") + line.count("S")
    print(line)

print()
print(f"Number of plots: {count}")







    
    