import re

def get_conforming(order_rules: list, update: list):
  for rule in order_rules:
    first_rule, second_rule = rule.split("|")

    if first_rule in update and second_rule in update:
      if update.index(first_rule) > update.index(second_rule):
        return

  return update

with open("5/input.txt", "r") as input_file:
  input = input_file.read()
  order_rules = re.findall(r"[0-9]+\|[0-9]+", input)
  numbers = re.sub(r"[0-9]+\|[0-9]+", "", input).strip()
  split_numbers = numbers.split("\n")

# Get the sum of the middle number in updates that confine to order_rules

conforming_updates = []
for num_line in split_numbers:
  update = num_line.split(",")
  
  conforming = get_conforming(order_rules, update)
  if conforming:
    conforming_updates.append(conforming)

middle_conforming = []
for update in conforming_updates:
  middle_conforming.append(int(update[int(len(update)/2)]))

print(sum(middle_conforming))