# Write a program in python that accepts a string to setup a passwords.
# Your entered password must meet the following requirements:
# * The password must be at least eight characters long.
# * It must contain at least one uppercase letter.
# * It must contain at least one lowercase letter.
# * It must contain at least one numeric digit.


while True:
    password = input("Please enter the password: ")

    if len(password) >= 8:
        pass
    else:
        print("Password should be at least 8 characters long!")
        print("Try again!")
        print()
        continue

    uppercase_letters_counter = 0
    lowercase_letters_counter = 0
    digits_counter = 0

    for character in password:
        if character.isupper():
            uppercase_letters_counter += 1
        elif character.islower():
            lowercase_letters_counter += 1
        elif character.isdigit():
            digits_counter += 1
        elif character.isspace():
            print("No space allowed")
            print("Try again!")
            print()
            break
    else:
        if uppercase_letters_counter > 0 and lowercase_letters_counter > 0 and digits_counter > 0:
            pass
        else:
            print("Password must contain one lowercase character, one uppercase character and one digit!")
            print("Try again!")
            print()
            continue

        print("Password accepted.")
        exit()
