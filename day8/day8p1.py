# read in input file
import re

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

# start at AAA, end at ZZZ
start, end = 'AAA', 'ZZZ'
ptr = start
fin = False
steps = 0
lp = len(pattern)

while fin == False:
    if ptr == 'ZZZ':
        fin = True
        break
    direction = pattern[steps % lp]
    # traverse in appropriate direction
    if direction == "R":
        ptr = mdict[ptr][1]
    else:
        ptr = mdict[ptr][0]
    # increment steps counter
    steps += 1

print(f"Steps taken: {steps}")


