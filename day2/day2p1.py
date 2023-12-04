# bag has 12 red cubes, 13 green and 14 blue cubes
# find the sum of IDs of valid games
# ie. red/green/blue should not exceed the values above

import re
# let's read in the file first
with open('input.txt', 'r') as f:
    file = f.read()

lines = file.split('\n')

# let's convert the lines into a dictionary
games_dict = dict()

# populate the keys with respective game nos.
for line in lines:
    game = line.split(":")
    game_num = int(game[0].split()[1])
    games_dict[game_num] = game[1]


# define a function to get the max number of balls for each colour for each game
def check_valid(color, entry):
    regex = "\d{1,2}(?= " + color + ")"
    draws = list(map(int,re.findall(regex, entry)))
    max_draw = max(draws)
    if color == "red":
        return max_draw <= 12
    if color == "green":
        return max_draw <= 13
    if color == "blue":
        return max_draw <= 14

sum = 0
# print(games_dict)
for k,v in games_dict.items():
    if check_valid("red", v) and check_valid("green", v) and check_valid("blue", v):
        sum += k
    
print(sum)


