# input string
# remove spaces at the beginning of the string
# print string

def remove_space(string):
    for i in range(len(string)):
        if string[i] != " ":
            return string[i:]
    return ""

user_input_string = str(input("Enter string: "))
no_space = remove_space(user_input_string)
print("result:", no_space)