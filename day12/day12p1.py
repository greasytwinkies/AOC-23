import re
from itertools import combinations

with open("input.txt", "r") as f:
    file = f.read()

lines = file.split('\n')

springs = []

for line in lines:
    match = re.search("([#?.]+) ([\d,]+)", line)
    springs.append((match.group(1), list(map(int, match.group(2).split(",")))))

totalcomb = 0

# calculate the number of remaining springs for each row
for row in springs:
    spr, arr = row[0], row[1]
    curr = spr.count("#")
    rspr = sum(arr) - curr
    print(spr, sep = "", end = " ")
    print(arr)
    # get all the indexes of "?"
    open_slots = []
    for index, item in enumerate(spr):
        if item == "?":
            open_slots.append(index)
    print(f"No. of springs left to fill: {rspr}, open slots: {open_slots}")
    # now get all combinations
    comb = list(combinations(open_slots, rspr))
    print(f"Possible ways to open slots: {comb}")
    print()
    # iterate over these combinations
    for c in comb:
        testspr = spr
        for num in c: # each element in each combination
            testspr = testspr[:num] + "#" + testspr[num+1:]
        print(testspr)
        # use regex to find new spring combinations
        # check if they match the original
        matches = re.findall("#+", testspr)
        # if len(matches) != len(arr):
        #     continue
        ncomb = [len(match) for match in matches]
        if ncomb == arr:
            print(f"Found a match: {testspr}")
            totalcomb += 1

print()
print(f"Total number of possible arrangements: {totalcomb}")
        





