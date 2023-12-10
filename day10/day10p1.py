# read in input file
global grid
global visited

with open("input.txt", "r") as f:
    file = f.read()

# convert into 2d arrac
lines = file.split('\n')
grid = [list(line) for line in lines]

for line in grid:
    print(line)

print()

"""
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but cour sketch doesn't show what shape the pipe has.
"""

# find coordinates of S
s = tuple()
# we will just determine the formation of S bc looking at the grid lol
for a, b in enumerate(grid):
    for c, d in enumerate(b):
        if d == 'S':
            rS, cS = a, c
            break

print(f"Coordinates of S: {rS, cS}")

# replace S with appropriate pipe formation
grid[rS][cS] = "F"

for line in grid:
    print(line)
print()

# distance from S to itself
# there will be two possible paths, since S (and each pipe) is connected to two other pipes
# furthest distance is the intersection of both paths (bfs)
# must maintain a visited list? → this can just be a distance list lol

visited = set()
queue = []

def eval_pipe(r, c):
        char = grid[r][c]
        if char == "|":
            return ((r-1, c), (r+1, c))
        elif char == "-":
            return ((r, c-1),  (r, c+1))
        elif char == "L": 
            return ((r-1, c), (r, c+1))
        elif char == "J": 
            return ((r, c-1), (r-1, c))
        elif char == "7":
            return ((r, c-1), (r+1, c))
        elif char == "F": 
            return ((r, c+1), (r+1, c))


def bfs(network, coord):
    visited = set()
    queue = [(coord, 0)]  # Each element in the queue is a tuple (coord, depth)
    
    while queue:
        curr, depth = queue.pop(0)
        r, c = curr
        pipe = network[r][c]
        print(f"Depth: {depth}, Pipe: {pipe}, Coord: {curr}")

        for adj in eval_pipe(r, c):
            if adj not in visited:
                visited.add(adj)
                queue.append((adj, depth + 1))


bfs(grid, (rS, cS))

    

    