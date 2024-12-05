import re

def get_non_conforming(order_rules: list, update: list):
  for rule in order_rules:
    first_rule, second_rule = rule.split("|")

    if first_rule in update and second_rule in update:
      if update.index(first_rule) > update.index(second_rule):
        return update
      
def make_conform(order_rules: list, update: list):
  solved = 0
  # I think this is inefficient as shit but it seems to work :D
  while solved < 9:
    for rule in order_rules:
      first_rule, second_rule = rule.split("|")

      if first_rule in update and second_rule in update:
        first_index, second_index = update.index(first_rule), update.index(second_rule)

        if first_index > second_index:
          update[second_index], update[first_index] = update[first_index], update[second_index]
    
    solved += 1
  return update
        

with open("5/input.txt", "r") as input_file:
  input = input_file.read()
  order_rules = re.findall(r"[0-9]+\|[0-9]+", input)
  numbers = re.sub(r"[0-9]+\|[0-9]+", "", input).strip()
  split_numbers = numbers.split("\n")

non_conforming_updates = []
for num_line in split_numbers:
  update = num_line.split(",")
  
  non_conforming = get_non_conforming(order_rules, update)
  if non_conforming:
    non_conforming_updates.append(non_conforming)

conforming_updates = []
for update in non_conforming_updates:
  made_to_conform = make_conform(order_rules, update)
  conforming_updates.append(made_to_conform)

middle_conforming = []
for update in conforming_updates:
  middle_conforming.append(int(update[int(len(update)/2)]))

print(sum(middle_conforming))

# 6187 too low D:
# 6204 CORRECT WTF