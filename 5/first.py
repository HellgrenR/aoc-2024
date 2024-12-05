import re

with open("5/input.txt", "r") as input_file:
  input = input_file.read()
  order_rules = re.findall(r"[0-9]+\|[0-9]+", input)
  numbers = re.sub(r"[0-9]+\|[0-9]+", "", input).strip()
  joined_numbers = numbers.replace("\n", ",")

print("order_rules: ", order_rules)
print("numbers: ", joined_numbers)

# 