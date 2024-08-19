# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Draw the Pattern
row = 0
while row < size:
    # Print a row of asterisks
    for col in range(size):
        print("*", ends="")
    # Move to next line after each row
    print()
    row += 1    