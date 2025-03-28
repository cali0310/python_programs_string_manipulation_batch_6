# Create a program that does the same functionality without using swapcase() function.
# Ask user input
# Convert uppercase letters to lowercase and lowercase letters to uppercase
# Print the swapped case string

def custom_swapcase(string):
    result = ''
    for char in string:
        if 'a' <= char <= 'z':  # If lowercase, convert to uppercase
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':  # If uppercase, convert to lowercase
            result += chr(ord(char) + 32)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result

statement = input("Enter statement: ")
print(f'"{custom_swapcase(statement)}"')