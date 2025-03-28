# Create a program that do the same functionality without using ljust() function.
# ask user input
# Calculate the length of string
# If the length is less than width
# Append (width - length) spaces to string
# Print the left-justified string

def custom_ljust(string, width):
    return string + ' ' * max(0, width - len(string))

statement = input("Enter statement: ")
width = int(input("Enter total width: "))
print(f'"{custom_ljust(statement, width)}"')