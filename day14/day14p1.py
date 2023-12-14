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
rotated = list(zip(*lines[::-1]))
rotated = [list(row) for row in rotated]

# for line in rotated:
#     print(line)
# print()
# shift round rocks northward (rightward in this case)
# start by iterating from the end
shifted = [[i for i in line] for line in rotated]

load = 0

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

# now count total loads:
for line in shifted:
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


            

            

        

