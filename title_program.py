# Create a program that does the same functionality without using title() function.
# Ask user input
# Split the string into words
# Capitalize the first letter of each word and convert the rest to lowercase
# Join the words back into a single string
# Print the title-cased string

def custom_title(string):
    words = string.split()  # Split string into words
    title_cased_words = [word[0].upper() + word[1:].lower() if word else '' for word in words]
    return ' '.join(title_cased_words)

statement = input("Enter statement: ")
print(f'"{custom_title(statement)}"')