# first, read in input file
with open("exampleinput.txt", "r") as f:
    file = f.read()

# split file into relevant segments
segments = file.split('\n\n')
# print(segments)

# first segment contains the relevant seeds, let's convert that into a list
# for part 2, each pair of numbers now represents a range of seeds
seeds = list(map(int,segments[0].split()[1:]))
seed_pairs = []
for i in range(0, len(seeds), 2):
    seed_pairs.append((seeds[i], seeds[i+1]))

print(seed_pairs)

# convert the rest of the mappings into arrays
arraymap = []
for segment in segments[1:]:
    mapping = segment.split('\n')[1:]
    mapping = [list(map(int, x.split())) for x in mapping]
    arraymap.append(mapping)

print(arraymap)

# try iterating from location to seed instead
# reverse list of maps, reverse all mappings
# check every location to see if it matches a seed range
# smallest location with a match is the location
arraymap.reverse()
print(arraymap)
loc = 0
found = False
while found == False:
    ptr = loc
    print(loc)
    for maps in arraymap:
        for m in maps:
            diff = m[0] - m[1]
            start, end = m[0], m[0]+m[2]-1
            if start <= ptr <= end:
                ptr -= diff
                break
            else:
                continue
    for pair in seed_pairs:
        if pair[0] <= ptr <= pair[0]+pair[1]-1:
            found = True
            break
    if found == False:
        loc += 1

print(f"Lowest location found: {loc}")

            



# for key, pair in enumerate(seed_pairs):
#     r = pair[-1]
#     for i in range(r):
#         seed = pair[0] + i
#         ptr = seed
#         for maps in arraymap:
#             for m in maps:
#                 diff = m[0] - m[1]
#                 start, end = m[1], m[1]+m[2]-1
#                 if start <= ptr <= end:
#                     ptr += diff
#                     break # stop iterating when a match is found
#                 else: # if ptr not in range, continue checking the other maps
#                     continue
#         seed2loc[seed] = ptr

# print(list(seed2loc.items()))
# print("Lowest location number:", min(list(seed2loc.values())))