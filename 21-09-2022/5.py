# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

def histogram(list_param):
    for integer in list_param:
        print("*" * integer)


list_of_integers = [4, 9, 7]

histogram(list_of_integers)