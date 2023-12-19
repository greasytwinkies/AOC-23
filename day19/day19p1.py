with open("input.txt", "r") as f:
    file = f.read()

# split file into two parts
wf, ratings = file.split("\n\n")
wf = wf.split('\n')
ratings = ratings.split('\n')

wfdict = dict()

# convert workflows into dictionaries
for w in wf:
    name, proc = w.split("{")
    wfdict[name] = proc.split(",")
    for i, item in enumerate(wfdict[name]):
        if ":" in item:
            item = tuple(item.split(":"))
            wfdict[name][i] = item
    wfdict[name][-1] = wfdict[name][-1][:-1]
    print(name, wfdict[name])
print()
for i, part in enumerate(ratings):
    part = part[1:-1] # remove brackets
    part = tuple(part.split(","))
    pdict = dict()
    for item in part:
        pdict[item[:1]] = int(item[2:])
    ratings[i] = pdict
    # since everything is sorted in x,m,a,s
    # can remove the headers

print(ratings)    
print()
# iterate over parts
# for workflow, start at in
# break when each workflow is accepted or rejected
# append accepted parts to accepted list

accepted = []

for part in ratings:
    curr = "in"
    end = False
    while not end:
        for operation in wfdict[curr]:
            if type(operation) == tuple:
                # break down the operation
                op = operation[0]
                param, sign, val = op[0], op[1], int(op[2:])
                if sign == ">":
                    if part[param] > val:
                        operation = operation[1]
                    else:
                        continue
                elif sign == "<":
                    if part[param] < val:
                        operation = operation[1]
                    else:
                        continue
            if operation == "A":
                accepted.append(part)
                end = True
                break
            elif operation == "R":
                end = True
                break
            else:
                curr = operation
                break

print(accepted)

acc_sum = sum([sum(x.values()) for x in accepted]) 

print(acc_sum)