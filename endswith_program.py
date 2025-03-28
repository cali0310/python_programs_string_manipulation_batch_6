# Create a program that do the same functionality without using endswith() function.
# ask user input and suffix to check
# check suffix
# return result
# print result

def ends_with(string, suffix):
    # Check if suffix is longer than string
    if len(suffix) > len(string):
        return False
    
    # Compare last characters
    return string[-len(suffix):] == suffix

# Get user input
user_string = input("Enter a string: ")
suffix_to_check = input("Enter suffix to check: ")

# Check if ends with suffix
result = ends_with(user_string, suffix_to_check)

# Print the result
print("Does the string end with the suffix?", result)