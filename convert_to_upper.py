#Create a program that do the same functionality without using isupper() function.
# ask user input
# convert to upper without isupper() function
# print string

user_input_string = str(input("Enter string: ")).lower()
upper_string = user_input_string.swapcase()
print(upper_string)