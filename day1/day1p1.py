import re

# first, read in input file
with open('input.txt', encoding = "utf-8") as f:
    file = f.read()

lines = file.split("\n")

digits = []
for line in lines:
    matches = re.findall("\d", line)
    digits.append(str(matches[0]) + str(matches[-1]))

sum = 0
for num in digits:
    sum += int(num)

print(sum)
