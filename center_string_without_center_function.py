# Create a program that do the same functionality without using center() function.
# ask user input
# ask width
# center the string
# print string

def custom_center(string, width):
    total_padding = max(0, width - len(string))
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    return ' ' * left_padding + string + ' ' * right_padding

statement = input("Enter statement: ")
width = int(input("Enter total width: "))
print(f'"{custom_center(statement, width)}"')