# Write a method in python to display the elements of list thrice if it is a number and display
# the element terminated with ‘#’ if it is not a number.
# Hint-: Use InBuilt Function isdigit()
# Refer below as a input:-
# mylist = ['41','DROND','Sunbeam', '13','ZARA']

mylist = ['41', 'DROND', 'Sunbeam', '13', 'ZARA']


def way1():

    for element in mylist:
        try:
            element = int(element)
            for index in range(3):
                print(element)

        except ValueError:
            print(element + '#')


way1()


def way2():
    for element in mylist:
        if element.isdigit():
            for iterator in range(3):
                print(element)
        else:
            print(element + '#')

way2()