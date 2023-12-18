with open("exampleinput.txt", "r") as f:
    file = f.read()

lines = file.split('\n')

plan = []

for line in lines:
    plan.append(line.split())

# create a grid
grid = [["." for x in range(20)] for y in range(20)]

# for line in grid:
#     for item in line:
#         print(item, end = " ")

r, c = int(len(grid)/2-1), int(len(grid)/2-1)

for entry in plan:
    direction, length, color = entry[0], int(entry[1]), entry[2]
    for i in range(1, length+1):
        if direction == "U":
            r -= 1
        elif direction == "D":
            r += 1
        elif direction == "L":
            c -= 1
        elif direction == "R":
            c += 1
        grid[r][c] = ("#", color)

ngrid = [[item[0] for item in line] for line in grid]
for line in ngrid:
    for item in line:
        print(item, end = " ")
    print()
print()

copy = ngrid

for index, line in enumerate(ngrid):
    nline = line
    if "#" not in line:
        continue
    else:
        # get indexes of upward hashes
        nhashes = []
        for i, item in enumerate(line):
            if index > 0:
                if item == "#" and ngrid[index-1][i] == "#":
                    nhashes.append(i)
        if not nhashes:
            continue
        for n, item in enumerate(line):
            if item == ".":
                rem_hash = [x for x in nhashes if x > n]
                num = len(rem_hash)
                if num % 2 == 0: # even number means that the point is outside the polygon
                    continue
                elif num % 2 == 1:
                    nline[n] = "O"
    copy[index] = nline
print()
area = 0
for line in copy:
    for item in line:
        if item == "O" or item == "#":
            area += 1
        print(item, end = " ")
    print()
print()

print(f"Area: {area}")








