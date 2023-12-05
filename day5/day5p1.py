# first, read in input file
with open("input.txt", "r") as f:
    file = f.read()

# split file into relevant segments
segments = file.split('\n\n')
# print(segments)

# first segment contains the relevant seeds, let's convert that into a list
seeds = list(map(int,segments[0].split()[1:]))
# print(seeds)

# convert the rest of the mappings into arrays
arraymap = []
for segment in segments[1:]:
    mapping = segment.split('\n')[1:]
    mapping = [list(map(int, x.split())) for x in mapping]
    arraymap.append(mapping)

print(arraymap)

seed2loc = dict()

for seed in seeds:
    ptr = seed # use this to traverse the mapping
    for maps in arraymap:
        for m in maps:
            diff = m[0] - m[1]
            start, end = m[1], m[1]+m[2]-1
            if start <= ptr <= end:
                ptr += diff
                break # stop iterating when a match is found
            else: # if ptr not in range, continue checking the other maps
                continue
    seed2loc[seed] = ptr

print(list(seed2loc.items()))
print("Lowest location number:", min(list(seed2loc.values())))