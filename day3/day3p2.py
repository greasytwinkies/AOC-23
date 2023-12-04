import re

with open("input.txt", "r") as f:
    file = f.read()

lines = file.split("\n")
# print(lines)

def search_row(gearpos, row):
    # check if there are two adjacent numbers in the same row first
    # 2 criteria:
    # 1. the gear position cannot be at the start or end of the row
    # 2. there must be a number at both gearpos+1 and gearpos-1 indexes, but not gearpos.
    # let's check criteria 1 first
    adj = []
    if 0 < gearpos < len(row)-1:
        # now check criteria 2
        if not row[gearpos].isnumeric() and row[gearpos-1].isnumeric() and row[gearpos+1].isnumeric():
            # splice the row at gearpos
            left_substr = row[:gearpos]
            right_substr = row[gearpos+1:]
            adj.append(re.findall("\d+", left_substr)[-1])
            adj.append(re.findall("\d+", right_substr)[0])
            return adj
    # now check for one adjacent number in the row
    # edge cases: first row and last row
    # for first row, adjacent number can only appear rightward (inclusive) of gearpos
    if gearpos == 0:
        if (row[gearpos].isnumeric() or row[gearpos+1].isnumeric()):
            adj.append(re.findall("\d+", row)[0])
    # same logic for last row, but flipped
    elif gearpos == len(row)-1:
        if (row[gearpos].isnumeric() or row[gearpos-1].isnumeric()):
            adj.append(re.findall("\d+", row)[-1])
    else: # all other cases (middle rows)
        # no number at gearpos
        if not row[gearpos].isnumeric():
            # number is either on the left or on the right
            if row[gearpos-1].isnumeric():
                substring = row[:gearpos]
                adj.append(re.findall("\d+", substring)[-1])
            elif row[gearpos+1].isnumeric():
                substring = row[gearpos+1:]
                adj.append(re.findall("\d+", substring)[0])
        else:
            # number at gearpos
            # 4 cases: number extends to left/right, a one digit number at gearpos, or three digits with the middle number at gearpos
            # three digit number
            if row[gearpos-1:gearpos+2].isnumeric():
                adj.append(row[gearpos-1:gearpos+2])
            # number extends to the left
            elif row[gearpos-1].isnumeric():
                substring = row[:gearpos+1]
                adj.append(re.findall("\d+", substring)[-1])
            # number extends to the right
            elif row[gearpos+1].isnumeric():
                substring = row[gearpos:]
                adj.append(re.findall("\d+", substring)[0])
            # 1 digit number at gearpos
            else:
                adj.append(row[gearpos])

    return adj

gears = []

for column, row in enumerate(lines):
    matches = re.finditer("\*", row)
    for match in matches:
        adj_num = []
        # store the position of the gear
        gearpos = match.span()[0]
        # we can start with the same row first
        # for same row as asterisk, number must either start or end one index after/before the asterisk
        if row[gearpos-1].isnumeric() and gearpos > 0:
            substring = row[:gearpos]
            adj_num.append(re.findall("\d+", substring)[-1])
        if row[gearpos+1].isnumeric() and gearpos < len(row)-1:
            substring = row[gearpos+1:]
            adj_num.append(re.findall("\d+", substring)[0])
        if column > 0:
            adj_num += search_row(gearpos, lines[column-1])
        if column < len(row)-1:
            adj_num += search_row(gearpos, lines[column+1])

        if len(adj_num) == 2:
            gears.append(adj_num)
        
print(gears)
# now lets get the gear ratios
gear_ratios = [int(gear[0]) * int(gear[1]) for gear in gears]
print(sum(gear_ratios))