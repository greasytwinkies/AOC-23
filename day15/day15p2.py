import re

with open("input.txt", "r") as f:
    file = f.read()

steps = file.split(",")
boxes = [[] for i in range(256)]
for step in steps:
    print(step)
    match = re.match("([a-z]+)([=-])(\d)?", step)
    label = match.group(1) 
    operation = match.group(2)
    if match.group(3):
        foc = int(match.group(3))
    else:
        foc = 0
    # run hash algorithm on label
    n = 0
    for char in label:
        n += ord(char)
        n *= 17
        n = n % 256
        print(n)
    if operation == "-":
        search = boxes[n]
        for i, box in enumerate(search):
            if box.startswith(label):
                del boxes[n][i]
                break
    elif operation == "=":
        search = boxes[n]
        found = False
        for i, box in enumerate(search):
            if box.startswith(label):
                boxes[n][i] = label + " " + str(foc)
                found = True
                break
        if not found:
            boxes[n].append(label + " " + str(foc))
    for x, box in enumerate(boxes):
        if box:
            print(f"Box {x}: {box}")

total = 0

for x, box in enumerate(boxes):
    for i, item in enumerate(box):
        power = ((x+1) * (i+1) * int(item[-1]))
        print(power)
        total += power

print(f"Total focusing power: {total}")
        
        
            





    # val = 0
    # for char in step:
    #     val += ord(char)
    #     val *= 17
    #     val = val % 256
    # vals.append(val)

# print(f"Sum of results: {sum(vals)}")

