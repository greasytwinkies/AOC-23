with open("input.txt", "r") as f:
    file = f.read()

lines = file.split('\n')

def convertLineToIntList(line):
    return list(map(int, line.split()))


lines = [convertLineToIntList(line) for line in lines]

def getListDiff(ilist):
    return [ilist[i+1] - ilist[i] for i, x in enumerate(ilist) if i < len(ilist)-1]

def find_next(list1, list2):
    if len(set(list2)) == 1:
        return list1[-1] + list2[-1]
    return list1[-1] + find_next(list2, getListDiff(list2))

sumnext = 0
for line in lines:
    sumnext += find_next(line, getListDiff(line))

print(f"Total sum of subsequent values: {sumnext}")




