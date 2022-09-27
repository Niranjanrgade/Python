# Write a program that accepts a list from user and print the alternate element of list

input_list = []


def list_filler():
    print("+ Please enter(Give) the list elements.")
    print("+ To stop(QUIT) entering(Filling) PRESS SPACEBAR.")

    while True:
        element = input("Enter element of list: ")
        if element.isspace():
            break
        else:
            input_list.append(element)


list_filler()

print(f"The alternate elements of list, '{input_list}' are: ")

for element in input_list[::2]:
    print(element, end=', ')

print("and")

for element in input_list[1::2]:
    print(element, end=', ')

print("respectively")

