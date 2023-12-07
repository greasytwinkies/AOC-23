import re
from collections import Counter

# read in input file
with open('input.txt', 'r') as f:
    file = f.read()

matches = re.finditer("([\dA-Z]{5}) (\d+)", file)
hands = [(match.group(1), int(match.group(2))) for match in matches]
print(hands)

rel_str =  "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")

# relative strength: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
# hands: 
    # 5 a kind, 4 a kind, full house (3,2), 3 a kind    
    # two pairs, one pair, high card (all distinct)
# tie-breaker: check strength of first card

# we need to order the set of hands first
# we can use set():
    # 5 a kind: len(set) == 1 (5)

    # 4 a kind: 2 (4, 1)
    # full house: 2 (3, 2)

    # 3 a kind: 3 (3, 1, 1)
    # two pairs: 3 (2, 2, 1)

    # one pair: 4 (2, 1, 1, 1)

    # high card: 5 (1, 1, 1, 1, 1)
def max_freq(hand):
    occurence_count = Counter(hand)
    return occurence_count.most_common(1)[0][-1]

# then multiply the earnings for the set with its rank
def eval(hand1, hand2):
    mf1, mf2 = max_freq(hand1), max_freq(hand2)
    # get highest frequency for each hand
    if mf1 > mf2: # hand1 lower rank than hand2
        return True
    elif mf1 == mf2:
        u1, u2 = len(set(hand1)), len(set(hand2))
        # tiebreaker 1: check the number of unique cards
        if u1 < u2:
            return True # hand 1 lower rank than hand 2
        elif u1 == u2:
            # tiebreaker 2: check cards
            for x, y in zip(hand1, hand2):
                rs1, rs2 = rel_str.index(x), rel_str.index(y)
                if rs1 < rs2:
                    return True
                elif rs1 > rs2:
                    return False
                else:
                    continue
        else:
            return False
    else:
        return False

n = len(hands)
for i in range(n):
    for j in range(0, n-i-1):
        # swap elements if element found has a lower strength than the following element
        if eval(hands[j][0], hands[j+1][0]):
            hands[j], hands[j+1] = hands[j+1], hands[j]

print(hands)
total_winnings = 0
for index, hand in enumerate(hands):
    rank = index+1
    total_winnings += hand[-1] * rank

print(f"Total winnings: {total_winnings}")
        



