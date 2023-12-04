# first, read in file
with open("input.txt", "r") as f:
    file = f.read()

lines = file.split("\n")

# create a dictionary with each card as the key
card_dict = dict()
for line in lines:
    card_no, numbers = line.split(":")
    card_no = int(card_no.split()[-1])
    winning_nums, own_nums = numbers.split("|")
    winning_nums = list(map(int, winning_nums.split()))
    own_nums = list(map(int, own_nums.split()))
    card_dict[card_no] = (winning_nums, own_nums)

""" for item in card_dict.items():
    print(item) """

# iterate over the values of the dictionary
# iterate over each item in winning_nums first
# for each element of winning_nums, iterate over all numbers in own_nums
# calculate the number of overlapping numbers (n)
# score for that card is 2 ** (n-1)
# let's create a new dictionary with the same keys
# the values of each card will be (matching_nums, card_score)


total_score = 0
card_nums = dict()

for k, v in card_dict.items():
    matching_nums = 0
    card_score = 0
    for n in v[0]:
        comparenum = n
        for n in v[1]:
            if n == comparenum:
                matching_nums += 1
    if matching_nums > 0:
        card_score = 2 ** (matching_nums-1)
    card_nums[k] = matching_nums

for item in card_nums.items():
    print(item)

def calc_cards(card_nums, k):
    if k > len(card_nums):
        return 0
    if card_nums[k] == 0:
        return 1
    invoked_cards = 0
    for i in range(1, card_nums[k]+1):
        invoked_cards += calc_cards(card_nums, k+i)
    return 1 + invoked_cards

total_cards = 0

for i in range(1, len(card_nums)+1):
    total_cards += calc_cards(card_nums, i)

print(total_cards)


