input_file = open("1/input.txt", "r")

list_1 = []
list_2 = []

for line in input_file:
  split_line = line.split("   ")

  list_1.append(int(split_line[0]))
  list_2.append(int(split_line[1].rstrip("\n")))

similarity_score = []

for first in list_1:
  # Loop through list_2, everytime n == list_2[i], multiplier++, then multiply n by multiplier
  multiplier = 0
  
  for second in list_2:
    if first == second:
      multiplier = multiplier + 1

  multiplied = first * multiplier

  similarity_score.append(multiplied)

sum_similarity_score = sum(similarity_score)
print(sum_similarity_score)