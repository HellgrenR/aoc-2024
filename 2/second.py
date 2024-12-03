input_file = open("2/input.txt", "r")
temp_file = open("2/temp.txt", "r")

# instruction summary
# Add dampener for one fault

def is_decreasing(int_row):
    score = 0
    for i in range(len(int_row) - 1):
        if int_row[i] <= int_row[i + 1]:
            score += 1
        elif int_row[i] - int_row[i + 1] > 3:
            return False
        if score > 1:
            return False

    return True
        
def is_increasing(int_row):
    score = 0
    for i in range(len(int_row) - 1):
        if int_row[i] >= int_row[i + 1]:
            score += 1
        elif int_row[i + 1] - int_row[i] > 3:
            return False
        if score > 1:
            return False

    return True
    
safe_rows = 0

for row in input_file:
    row_list = row.split(" ")
    
    safe = 0

    int_rows = []
    for row in row_list:
       column = int(row)
       int_rows.append(column)

    has_increased = is_increasing(int_rows)
    has_decreased = is_decreasing(int_rows)

    print(int_rows)
    print("Increases: ", has_increased)
    print("Decreases: ", has_decreased)

    if has_increased == True or has_decreased == True:
        safe = 1

    safe_rows += safe
    print(safe_rows)
    print()


print(safe_rows)


