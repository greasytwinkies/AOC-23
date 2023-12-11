import itertools

with open('input.txt', 'r') as f:
    file = f.read()

lines = file.split('\n')

for line in lines:
    for x in line:
        print(x, end = " ")
    print()
print()
# find lines that contain no galaxies
def expand(image):
    expanded = [[x for x in row] for row in image]
    expansion = 0
    for x in range(len(image)):
        line = expanded[x+expansion]
        if set(line) == set('.') or set(line) == set([".", "?"]):
            # line does not contain galaxies, expand
            expanded.insert(x+expansion, ["?" for x in line])
            expansion += 1

    return expanded

expanded = expand(lines)
for line in expanded:
    for x in line:
        print(x, end = " ")
    print()

print()

# now for outward expansion
# rotate array cw, then expand
# rotate array back to original alignment

rotated = list(zip(*expanded[::-1]))
for line in rotated:
    for x in line:
        print(x, end = " ")
    print()
print()

rotated = expand(rotated)
for line in rotated:
    for x in line:
        print(x, end = " ")
    print()
print()
for i in range(3):
    rotated = list(zip(*rotated[::-1]))

expanded = rotated

for line in expanded:
    for x in line:
        print(x, end = " ")
    print()
print()
# now let's assign a unique number to each of the galaxies
count = 0
labelled = [[x for x in row] for row in expanded]
gdict = dict()
for index, line in enumerate(expanded):
    for i, x in enumerate(line):
        if x == "#":
            count += 1
            labelled[index][i] = count
            gdict[count] = index, i

for line in labelled:
    for x in line:
        print(x, end = " ")
    print()

pairs = list(itertools.combinations([x for x in range(1, count+1)], 2))
print(pairs)
print(len(pairs))

for item in gdict.items():
    print(item)
# now to find the shortest path between pairs
# to find shortest path, just use bfs (LMAO)       

def neighbors(coord1, coord2, grid):
    neighbors = []
    r1, c1 = coord1
    r2, c2 = coord2
    # check general direction of travel. ie no need to bfs the other way lol
    if r2 >= r1: # g2 is lower or equal row as g1 (search downwards)
        if r1 < len(grid) - 1:
            neighbors.append((r1+1, c1))
    if r2 <= r1: # g2 higher than g1 (search upwards)
        if r1 > 0:
            neighbors.append((r1-1, c1))
    if c2 >= c1: # c2 to the right of c1 (search rightwards)
        if c1 < len(grid[r1])-1:
            neighbors.append((r1, c1+1))
    if c2 <= c1: # c2 to the left of c1 (search leftwards)
        if c1 > 0:
            neighbors.append((r1, c1-1))
    return neighbors

def bfs(grid, c1, c2):
    visited = set()
    queue = [(c1, 0)]  # Each element is a tuple (node, depth)
    found = False

    while queue:
        current, depth = queue.pop(0)
        #print(f"Node: {current}, Depth: {depth}")
        if current == c2:
            found = True
            break

        # Explore neighbors of the current node (n, s, e, w - no diagonal moves)
        for neighbor in neighbors(current, c2, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                r, c = neighbor[0], neighbor[1]
                if grid[r][c] != "?":
                    queue.append((neighbor, depth + 1))  # Increment depth for the neighbor
                else:
                    queue.append((neighbor, depth + 1000000-1))

    if found:
        print(f"Shortest distance from {c1} to {c2}: {depth}")
        return depth
    else:
        print("Destination not reachable.")

shortest_dists = []
for pair in pairs:
    g1, g2 = pair[0], pair[1]
    c1, c2 = gdict[g1], gdict[g2] # coordinates of galaxy
    shortest_dists.append(bfs(expanded, c1, c2))

print(shortest_dists)
print(sum(shortest_dists))
