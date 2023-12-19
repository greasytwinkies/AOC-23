import re
import math

with open("input.txt", "r") as f:
    file = f.read()

instructions = file.split('\n\n')[0].split('\n')

for index, line in enumerate(instructions):
    line = re.sub('[a-z]{2,}','\g<0>1', line)
    instructions[index] = line

instructions_divided = []

for line in instructions:
    commas = line.count(",")
    if commas == 1:
        instructions_divided.append(line)
    else:
        title = line.split("{")[0][:-1]
        # split instructions on comma
        # merge last two 
        line = line.split(",")
        line[-2] += "," + line[-1]
        line = line[:-1]
        count = 1
        for i in range(len(line)):
            if 0 <= i < len(line)-1:
                line[i] = line[i] + "," + title + str(count+1) + "}"
            if 0 < i <= len(line)-1:
                line[i] = title + str(count) + "{" + line[i]
            count += 1
        instructions_divided += line

global idict; idict = dict()
for line in instructions_divided:
    match = re.search("(\w+){([xmas])([<>])(\d+):(\w+),(\w+)}", line)
    idict[match.group(1)] = [match.group(2), match.group(3), int(match.group(4)), match.group(5), match.group(6)]
    
# for item in idict.items():
#     print(item)

global accepted; accepted = []

r = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
def process_range(r, target):
    if target == "A":
        accepted.append(r)
        return
    elif target == "R":
        return
    v = idict[target]
    cat, operand, val, dest1, dest2 = v
    rrange = r[cat]
    rmin, rmax = rrange
    if operand == "<":
        # 3 scenarios:
        # 1. max of range is smaller than val → pass in same range with dest1
        # 2. min of range is larger than val → pass in same range with dest2
        # 3. range is split → split ranges then call separate functions with each destination
        if rmax < val:
            process_range(r, dest1)
        elif rmin >= val:
            process_range(r, dest2)
        else: 
            r1 = r.copy()
            r1[cat] = (rmin, val-1)
            r2 = r.copy()
            r2[cat] = (val, rmax)
            process_range(r1, dest1)
            process_range(r2, dest2)
    elif operand == ">":
        if rmin > val:
            process_range(r, dest1)
        elif rmax <= val:
            process_range(r, dest2)
        else: 
            r1 = r.copy()
            r1[cat] = (rmin, val)
            r2 = r.copy()
            r2[cat] = (val+1, rmax)
            process_range(r1, dest2)
            process_range(r2, dest1)

process_range(r, "in1")

total = 0

for entry in accepted:
    amts = [x[-1]-x[0]+1 for x in entry.values()]
    prod = math.prod(amts)
    print(amts)
    print(prod)
    total += prod

print(total)
    



    


        






