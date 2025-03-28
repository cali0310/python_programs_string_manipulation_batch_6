# Create a program that do the same functionality without using removeprefix() function.
# ask user input
# remove prefix 
# return remaining string characters
# print string

def remove_prefix(string, prefix):
    if string.startswith(prefix):
        return string[len(prefix):]
    return string

user_input_string = str(input("Enter string: "))
prefix_to_remove = input("Enter prefix to remove: ")
no_prefix = remove_prefix(user_input_string, prefix_to_remove)
print("Result: ", no_prefix)