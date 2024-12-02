input_file = open("2/input.txt", "r")

# instruction summary
# Find out if a row is safe.
# GET TOTAL AMOUT OF SAFE ROWS
# Safe: each index of the row is either increasing or decreasing, not a mix
# Safe: each index differs by at least 1 and at most 3
# Safe ex: 2 5 6 8
# Unsafe ex: 1 6 5 5

def is_decreasing(int_row):
    for i in range(len(int_row) - 1):
        if int_row[i] <= int_row[i + 1]:
            return False
        elif int_row[i] - int_row[i + 1] > 3:
            return False
        
    return True
        
def is_increasing(int_row):
    for i in range(len(int_row) - 1):
        if int_row[i] >= int_row[i + 1]:
            return False
        elif int_row[i + 1] - int_row[i] > 3:
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

    if is_increasing(int_rows) == True or is_decreasing(int_rows) == True:
        safe = 1

    safe_rows = safe_rows + safe


print(safe_rows)


