import copy

# read in input file
with open("input.txt", "r") as f:
    file = f.read()

lines = file.split('\n')
lines = [[x for x in line] for line in lines]
# for line in lines:
#     print(line)
# print()
# file only has one platform
# let's rotate platform clockwise so it's easier to iterate

# for line in rotated:
#     print(line)
# print()
# shift round rocks northward (rightward in this case)
# start by iterating from the end
shifted = [[i for i in line] for line in lines]

rotated = shifted

load = 0

for n in range(1000):
    for a in range(4):
        # tilt north: rotate platform 90 deg cw, tilt east, rotate back
        # tilt west: rotate platform 180, tilt east, rotate back OR reverse?
        # tilt south: rotate platform 270 deg cw, tilt east, rotate back
        # tilt east: tilt normally
        if a == 0: # north
            rotated = list(zip(*rotated[::-1]))
            rotated = [list(row) for row in rotated]
        elif a == 1: # west
            rotated = list(zip(*rotated[::-1]))
            rotated = list(zip(*rotated[::-1]))
            rotated = [list(row) for row in rotated]
        elif a == 2: # south
            rotated = list(zip(*rotated[::-1]))
            rotated = list(zip(*rotated[::-1]))
            rotated = list(zip(*rotated[::-1]))
            rotated = [list(row) for row in rotated]
        elif a == 3: # east
            pass
        for i, line in enumerate(rotated):
            line_copy = line
            for x in range(len(line_copy)-2, -1, -1):
                item = line_copy[x]
                if item == "O":
                    print(x)
                    # shift item rightwards until
                    # another O, # or boundary is met
                    # iterate starting from x + 1 to end
                    flag = False
                    for y in range(x+1, len(line_copy)):
                        search = line_copy[y]
                        if search == "O" or search == "#":
                            # shift round rock to y-1
                            if y-1 != x:
                                line_copy[y-1] = "O"
                                # replace the original index with nothing
                                line_copy[x] = "."
                            flag = True
                            break
                    # if exit successfully from loop, means remaining path is clear
                    # shift round rock to end of the line
                    if not flag:
                        line_copy[len(line_copy)-1] = "O"
                        line_copy[x] = "."
            shifted[i] = line_copy
        rotated = shifted
        # rotate back
        if a == 0: # north
            rotated = list(zip(*rotated[::-1]))
            rotated = list(zip(*rotated[::-1]))
            rotated = list(zip(*rotated[::-1]))
            rotated = [list(row) for row in rotated]
        elif a == 1: # west
            rotated = list(zip(*rotated[::-1]))
            rotated = list(zip(*rotated[::-1]))
            rotated = [list(row) for row in rotated]
        elif a == 2: # south
            rotated = list(zip(*rotated[::-1]))
            rotated = [list(row) for row in rotated]
        for line in rotated:
            print(line)
print()

rotated = list(zip(*rotated[::-1]))
rotated = [list(row) for row in rotated]
for line in rotated:
    for x in range(len(line)-1, -1, -1):
        item = line[x]
        if item == "O":
            load = load + x + 1

print(f"Total load: {load}")
        

# # rotate back to check
# for i in range(3):
#     shifted = list(zip(*shifted[::-1]))
# shifted = [list(row) for row in shifted]
# for line in shifted:
#     print(line)


