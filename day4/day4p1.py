# first, read in file
with open("input.txt", "r") as f:
    file = f.read()

lines = file.split("\n")

# create a dictionary with each card as the key
card_dict = dict()
for line in lines:
    card_no, numbers = line.split(":")
    card_no = card_no.split()[-1]
    winning_nums, own_nums = numbers.split("|")
    winning_nums = winning_nums.split()
    own_nums = own_nums.split()
    card_dict[card_no] = (winning_nums, own_nums)

""" for item in card_dict.items():
    print(item) """

# iterate over the values of the dictionary (key not needed right now)
# iterate over each item in winning_nums first
# for each element of winning_nums, iterate over all numbers in own_nums
# calculate the number of overlapping numbers (n)
# score for that card is 2 ** (n-1)

total_score = 0

for v in card_dict.values():
    matching_nums = 0
    card_score = 0
    for n in v[0]:
        comparenum = n
        for n in v[1]:
            if n == comparenum:
                matching_nums += 1
    if matching_nums > 0:
        card_score = 2 ** (matching_nums-1)
    print(card_score)
    total_score += card_score

print(total_score)