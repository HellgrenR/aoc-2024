import re

with open("3/input.txt", "r") as input_file:
  lines = input_file.read()
  joined_lines = lines.replace("\n", "")

# find between don't() and do(), and remove it

multiplied_numbers = []

removed = re.sub(r"don't\(\).*?(do\(\)|$)", "", joined_lines)
regexed = re.findall(r"mul\([0-9]+,[0-9]+\)", removed)

for mul_numbers in regexed:
  numbers = re.findall("([0-9]+),([0-9]+)", mul_numbers)

  multiplied_number = int(numbers[0][0]) * int(numbers[0][1])

  multiplied_numbers.append(multiplied_number)

print(sum(multiplied_numbers))

# 110269523 too high HellgrenR
# 83596704 too high
# 69247082 incorrect
# 63013756 CORRECT HAD TO REMOVE ALL NEWLINES