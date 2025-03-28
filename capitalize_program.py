# Create a program that does the same functionality without using capitalize() function.
# Ask user input
# Convert the first character to uppercase
# Convert all other characters to lowercase
# Print the capitalized string

def custom_capitalize(string):
    if not string:
        return string  # Return empty string if input is empty
    return string[0].upper() + string[1:].lower()

statement = input("Enter statement: ")
print(f'"{custom_capitalize(statement)}"')