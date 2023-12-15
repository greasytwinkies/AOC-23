with open("exampleinput.txt", "r") as f:
    file = f.read()

steps = file.split(",")
vals = []
for step in steps:
    print(step)
    val = 0
    for char in step:
        val += ord(char)
        val *= 17
        val = val % 256
    print(val)
    vals.append(val)

print(f"Sum of results: {sum(vals)}")

