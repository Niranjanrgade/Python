# Write a program that reads a string from keyboard and display:
# * The number of uppercase letters in the string
# * The number of lowercase letters in the string
# * The number of digits in the string
# * The number of whitespace characters in the string


print('*' * 100)

input_string = input("Please enter the text which is to be processed: ")

print('*' * 100)

uppercase_letters_counter = 0
lowercase_letters_counter = 0
digits_counter = 0
whitespace_counter = 0

for character in input_string:
    # The number of uppercase letters in the string
    if character.isupper():
        uppercase_letters_counter += 1

    # The number of lowercase letters in the string
    elif character.islower():
        lowercase_letters_counter += 1

    # The number of digits in the string
    elif character.isdigit():
        digits_counter += 1

    # The number of whitespace characters in the string
    elif character.isspace():
        whitespace_counter += 1


print(f'The number of uppercase letter(s) in input string, "{input_string}" is/are {uppercase_letters_counter}.')
print('*' * 100)

print(f'The number of lowercase letter(s) in input string, "{input_string}" is/are {lowercase_letters_counter}.')
print('*' * 100)

print(f'The number of digit(s) in input string, "{input_string}" is/are {digits_counter}.')
print('*' * 100)

print(f'The number of whitespace character(s) in input string, "{input_string}" is/are {whitespace_counter}.')
print('*' * 100)
