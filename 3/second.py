import re

input_file = open("3/input.txt", "r")

enabled = True
# find between don't() and do(), and remove it
removed = re.sub("don't\(\).*?(do\(\)|$)", "", input_file.read())
regexed = re.findall("mul\([0-9]+,[0-9]+\)", removed)

multiplied_numbers = []

for mul_numbers in regexed:
  numbers = re.findall("([0-9]+),([0-9]+)", mul_numbers)

  multiplied_number = int(numbers[0][0]) * int(numbers[0][1])

  multiplied_numbers.append(multiplied_number)

print(sum(multiplied_numbers))

# 83596704 too high