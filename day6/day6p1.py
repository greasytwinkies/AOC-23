import math

# read in input
with open('input.txt', 'r') as f:
    file = f.read()

lines = file.split('\n')
# first line contains times, second line contains distances.
times = list(map(int,lines[0].split(":")[-1].strip().split()))
distances = list(map(int,lines[1].split(":")[-1].strip().split()))

races = list(zip(times, distances))
print(races)

# find the number of ways to beat the record for each race
# multiply the total number for each race
ways_to_beat_record = []

for time, record in races:
    ways = 0
    for x in range(1, time):
        # boat will not move for 0 or time
        # x will represent button hold time/speed
        move = time - x
        dist = move * x
        if dist > record:
            ways += 1
    ways_to_beat_record.append(ways)

print(f"Product of number of ways to beat record in all races: {math.prod(ways_to_beat_record)}")
        

