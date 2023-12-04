# find maximum number of cubes per colour per game
# power of set: multiply numbers of each colour together
# finally, find the sum of each power of each game

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


# define a function to get the max number of each colour of each game
def get_max(color, entry):
    regex = "\d{1,2}(?= " + color + ")"
    draws = list(map(int,re.findall(regex, entry)))
    max_draw = max(draws)
    return max_draw


sum = 0
# print(games_dict)
for k,v in games_dict.items():
    power = get_max("red", v) * get_max("green", v) * get_max("blue", v)
    sum += power

print(sum)


