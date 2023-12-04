import re
global symbols

# first, read in file
with open("input.txt", "r") as f:
    file = f.read()

lines = file.split("\n")
print(lines)

# let's get the total sum of all numbers first
nums = []
for line in lines:
    nums += list(map(int, re.findall("\d+", line)))

# print(nums)
# print(sum(nums))

# let's get a list of all symbols
filestring = ("").join(lines)
symbols = set(re.findall("[^\d\.]", filestring))
print(symbols)

# part numbers are numbers that are adjacent to a symbol
# we now have two possible approaches:
# either find the sum of all numbers adjacent to a symbol
# OR find all numbers that are not adjacent to a symbol
# and then minus that number from the total sum
# let's try the second one

# use regex to match occurrences of numbers
# use re.span() to store the starting and ending indexes of number
# splice corresponding rows and check that none of the elements are found in symbols
# search:
    # row above and row below: one index before first digit -> one index after last digit
    # corresponding row: one index before first digit, one index after last digit.
        # could potentially speed this up by just checking this during the original iteration

invalid_nums = []
def search(start, end, column, lines):
    searchstr = lines[column][start:end]
    if not re.findall("[^\d\.]", searchstr): # no symbols found, number is invalid
        return True
    return False # number is valid


def search_adjacent(start, end, column, lines, row):
    # need to handle start and end of row
    # as well as first and last columns
    if start > 0:
        start -= 1
    if end < len(row):
        end += 1
    if column == 0:
        return search(start, end, column+1, lines)
    elif column == len(lines)-1:
        return search(start, end, column-1, lines)
    else:
        return search(start, end, column-1, lines) and search(start, end, column+1, lines)


for column, row in enumerate(lines):
    matches = re.finditer("\d+", row)
    for match in matches:
        start, end = int(match.span()[0]), int(match.span()[1])
        # we can check if there are any symbols adjacent to the number on the same row
        if start > 0:
            noPrecedingSymbol = row[start-1] not in symbols
        else:
            noPrecedingSymbol = True
        if end < len(row):
            noFollowingSymbol = row[end] not in symbols
        else:
            noFollowingSymbol = True
        noSameRowSymbol = noFollowingSymbol and noPrecedingSymbol
        invalid = noSameRowSymbol and search_adjacent(start, end, column, lines, row)
        if invalid:
            invalid_nums.append(match.group())

invalid_nums = [int(x) for x in invalid_nums]

print(invalid_nums)

sum_valid = sum(nums) - sum(invalid_nums)
print(sum_valid)

            








        






