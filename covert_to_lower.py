# Create a program that do the same functionality without using lower() function.
# ask user input 
# convert to lower
# print string

user_input_string = str(input("Enter string: ")).upper()
lower_string = user_input_string.swapcase()
print(lower_string)