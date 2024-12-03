import re

input_file = open("3/input.txt", "r")
# Find all mul(x,y) and get the sum of all multiplications.

regexed = re.findall("mul\([0-9]+,[0-9]+\)", input_file.read())

multiplied_numbers = []

for mul_numbers in regexed:
  numbers = re.findall("([0-9]+),([0-9]+)", mul_numbers)

  multiplied_number = int(numbers[0][0]) * int(numbers[0][1])

  multiplied_numbers.append(multiplied_number)

print(sum(multiplied_numbers))




