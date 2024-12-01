input_file = open("1/input.txt", "r")

list_1 = []
list_2 = []

for line in input_file:
  split_line = line.split("   ")

  list_1.append(split_line[0])
  list_2.append(split_line[1].rstrip("\n"))

sorted_1 = sorted(list_1)
sorted_2 = sorted(list_2)

differences = []

for i in range(0, len(sorted_1)):
  first_list = int(sorted_1[i]) 
  second_list= int(sorted_2[i]) 

  if first_list > second_list:
    temp_distance = first_list - second_list
  elif first_list < second_list:
    temp_distance = second_list - first_list
  else:
    temp_distance = 0

  differences.append(temp_distance)

diff_sum = sum(differences)
print(diff_sum)
