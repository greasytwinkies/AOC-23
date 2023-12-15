import copy
# read in input
with open('input.txt', 'r') as f:
    file = f.read()

patterns = file.split('\n\n')
patterns = [x.split('\n') for x in patterns]

# find line of reflection by testing pairs of adjacent rows/columns
# check if reflection extends to at least one end of the pattern. (could be a red herring)

fsum = 0

def find_mirror(pattern, align, prev = -1):
    if align == 1: # check for vertical mirror, rotate pattern
        pattern = list(zip(*pattern[::-1]))
    for x in range(len(pattern)-1):
        if pattern[x] == pattern[x+1]: # possible reflection
            valid = True
            # check that the reflection extends until at least one side of the pattern
            for y in range(1, x+1):
                l, r = x-y, x+1+y
                # if r overfills, that means that end of pattern is reached
                if r == len(pattern):
                    if align == 1:
                        return x+1
                    elif align == 0:
                        return (x+1) * 100
                if pattern[l] != pattern[r]: # asymmetrical, break from loop and keep searching
                    valid = False
                    break
            # if exit from loop successfully, that means the mirror is valid
            if valid:
                if align == 1:
                    if prev != x+1:
                        return x+1
                    else:
                        continue
                elif align == 0:
                    if prev != (x+1)*100:
                        return (x+1)*100
                    else:
                        continue

            # increment sum
    return 0
    # if no horizontal match, must be vertical
    # rotate pattern clockwise 90 and carry out the same tests

error = []
count = 0

for pattern in patterns:
    found = False
    for i, row in enumerate(pattern):
        if found:
            break
        for x in range(len(row)):
            pattern_copy = copy.deepcopy(pattern)  # Make a deep copy to preserve changes
            element = row[x]
            if element == "#":
                pattern_copy[i] = pattern_copy[i][:x] + "." + pattern_copy[i][x + 1:]
            elif element == ".":
                pattern_copy[i] = pattern_copy[i][:x] + "#" + pattern_copy[i][x + 1:]

            oldpts = find_mirror(pattern, 0) + find_mirror(pattern, 1)
            h, v = find_mirror(pattern_copy, 0, oldpts), find_mirror(pattern_copy, 1, oldpts)
            if h==0 and v==0:
                pattern_copy = copy.deepcopy(pattern)
                continue
            # there is at least one non zero value
            # first case: both values are non zero
            # at least one of the cases will be correct
            if h>0 and v>0:
                if h==oldpts:
                    newpts = v
                elif v==oldpts:
                    newpts = h
            # second case: only one non zero value
            # may or may not be same as oldpts 
            elif h>0:
                if h==oldpts:
                    pattern_copy = copy.deepcopy(pattern)
                    continue
                else:
                    newpts = h
            elif v>0:
                if v==oldpts:
                    pattern_copy = copy.deepcopy(pattern)
                    continue
                else:
                    newpts = v
            
            print(h, v, oldpts, newpts)
            fsum += newpts
            count += 1
            found = True
            break
    if found == False:
        for line in pattern:
            error.append(pattern)


print(f"Final sum: {fsum}")
print(f"Debug: {count}/{len(patterns)}")

for pattern in error:
    found = False
    pattern_copy = copy.deepcopy(pattern)   
    for i, row in enumerate(pattern):
        if found:
            break
        for x in range(len(row)):
            pattern_copy = copy.deepcopy(pattern)  # Make a deep copy to preserve changes
            element = row[x]
            if element == "#":
                pattern_copy[i] = pattern_copy[i][:x] + "." + pattern_copy[i][x + 1:]
            elif element == ".":
                pattern_copy[i] = pattern_copy[i][:x] + "#" + pattern_copy[i][x + 1:]

            for line in pattern_copy:
                print(line)
            h, v = find_mirror(pattern_copy, 0), find_mirror(pattern_copy, 1)
            oldpts = find_mirror(pattern, 0) + find_mirror(pattern, 1)
            print(h, v, oldpts)
            print()
            if h==0 and v==0:
                pattern_copy = copy.deepcopy(pattern)
                continue
            # there is at least one non zero value
            # first case: both values are non zero
            # at least one of the cases will be correct
            if h>0 and v>0:
                if h==oldpts:
                    newpts = v
                elif v==oldpts:
                    newpts = h
            # second case: only one non zero value
            # may or may not be same as oldpts 
            elif h>0:
                if h==oldpts:
                    pattern_copy = copy.deepcopy(pattern)
                    continue
                else:
                    newpts = h
            elif v>0:
                if v==oldpts:
                    pattern_copy = copy.deepcopy(pattern)
                    continue
                else:
                    newpts = v
            
            print(h, v, oldpts, newpts)
            fsum += newpts
            count += 1
            found = True
            break



