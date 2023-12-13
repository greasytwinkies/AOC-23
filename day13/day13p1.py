# read in input
with open('input.txt', 'r') as f:
    file = f.read()

patterns = file.split('\n\n')
patterns = [x.split('\n') for x in patterns]

# find line of reflection by testing pairs of adjacent rows/columns
# check if reflection extends to at least one end of the pattern. (could be a red herring)

fsum = 0

def find_mirror(pattern, align):
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
                    return x+1
                elif align == 0:
                    return (x+1)*100

            # increment sum
    return 0
    # if no horizontal match, must be vertical
    # rotate pattern clockwise 90 and carry out the same tests

for index, pattern in enumerate(patterns):
    pts = (find_mirror(pattern, 1) + find_mirror(pattern, 0))
    fsum += pts
    if pts == 0:
        for line in pattern:
            print(line)
        print(f"Pattern {index}")
        print()
    # for line in pattern:
    #     print(line)
    # print(f"Pattern {index}: {pts} pts")
    # print()

            
print(f"Final sum: {fsum}")
        


        
        
