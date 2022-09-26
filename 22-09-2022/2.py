# Display following menu and write required function for it
# A. Display characters from even position
# B. Display characters from odd position
# C. Display length of a string
# D. Add a at the end of string length times

print()
print("Welcome!")

while True:

    print()
    print("Press 'A' To Display characters from even position ")
    print("Press 'B' To Display characters from odd position")
    print("Press 'C' To Display length of a string")
    print("Press 'D' To Add a at the end of string length times")
    print("Press anything to exit.")

    print()
    choice = input("Enter the choice: ")

    print()
    string_text = input("Enter the string to be processed:")

    print()
    if choice == 'A' or choice == 'a':
        print(f"Characters from even position: {string_text[1::2]}")
        print()
    elif choice == 'B' or choice == 'b':
        print(f"Characters from odd position: {string_text[0::2]}")
        print()
    elif choice == 'C' or choice == 'c':
        print(len(string_text))
        print()
    elif choice == 'D' or choice == 'd':
        formatted_string = string_text + 'a' * len(string_text)
        print(formatted_string)
        print()
    else:
        break
