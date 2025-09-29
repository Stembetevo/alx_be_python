# Define the height of the pyramid
rows = 5

# Outer for loop to control the number of rows
for current_row in range(1, rows + 1):
    
    # First inner for loop: Print spaces to center the pyramid
    # Number of spaces = (total rows - current row)
    spaces_needed = rows - current_row
    for space in range(spaces_needed):
        print(" ", end="")
    
    # Second inner for loop: Print asterisks for the current row
    # Number of asterisks = (2 * current_row - 1) for a proper pyramid
    asterisks_needed = 2 * current_row - 1
    for asterisk in range(asterisks_needed):
        print("*", end="")
    
    # Move to next line after completing current row
    print()