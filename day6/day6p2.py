import math

# read in input
with open('input.txt', 'r') as f:
    file = f.read()

lines = file.split('\n')
# part 2: the numbers are now part of one whole number
time = int("".join(lines[0].split(":")[-1].strip().split()))
record = int("".join(lines[1].split(":")[-1].strip().split()))

print(time, record)

ways_to_beat_record = 0

for x in range(1, time):
    move = time - x
    dist = move * x
    if dist > record:
        ways_to_beat_record += 1

print(f"Ways to beat record: {ways_to_beat_record}")
        

