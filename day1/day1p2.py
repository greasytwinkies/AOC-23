import re

# first, read in input file
with open('input.txt', encoding = "utf-8") as f:
    file = f.read()

lines = file.split("\n")

# find first and last digit of each line
# digits can be represented as numbers or text strings
# let's create a dictionary to handle text strings

word2num =     {"one":"1",
                "two":"2",
                "three":"3",
                "four":"4",
                "five":"5",
                "six":"6",
                "seven":"7",
                "eight":"8",
                "nine":"9"
                }

# let's create a function to convert words to their corresponding digits
# based on the dictionary

def convert_word2num(word):
    return word2num.get(word, word)


# let's find the first digit first
digits = []
regex = "(one|two|three|four|five|six|seven|eight|nine|\d)"
for line in lines:
    # use re.search since digit may not necessarily be at start of string
    first_digit = convert_word2num(re.search(regex, line).group())
    digits.append(first_digit)

print(digits)

# now let's find the last digit
regex = ".*(one|two|three|four|five|six|seven|eight|nine|\d)"
for index, line in enumerate(lines):
    last_digit = convert_word2num(re.search(regex, line).group(1))
    digits[index] += last_digit


print(digits)
# check that each element of list only contains 2 digits
# print([len(x[0]) for x in digits])

# now we just need to add up all the digits
sum = 0
for digit in digits:
    sum += int(digit)

print(sum)


