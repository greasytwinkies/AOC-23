# read in input file
import re
import math

with open("input.txt", "r") as f:
    file = f.read()

lines = file.split('\n')
print(lines)

# convert graph into a dictionary

pattern = lines[0]
mdict = dict()
for line in lines[2:]:
    match = re.match("(\w{3}) = \((\w{3}), (\w{3})\)", line)
    node, neighbors = match.group(1), (match.group(2), match.group(3))
    mdict[node] = neighbors

for item in mdict.items():
    print(item)

# start at all nodes that end with A
# end with all nodes that end with Z
# number of nodes that start with A is the same as the number of nodes that end with Z

ptrs = [x for x in mdict.keys() if x.endswith("A")]

steps = 0
lp = len(pattern)

# pattern loops from the first time node encounters another node ending in Z
# just that A is replaced with Z
# answer is just LCM of steps required to reach first Z node for each node

stepstofirstZ = []

for node in ptrs:
    steps = 0
    ptr = node
    while not ptr.endswith("Z"):
        direction = pattern[steps % lp]
        # traverse in appropriate direction
        if direction == "R":
            ptr = mdict[ptr][1]
        else:
            ptr = mdict[ptr][0]
        steps += 1
    stepstofirstZ.append(steps)
    

print(f"Steps taken: {math.lcm(*stepstofirstZ)}")