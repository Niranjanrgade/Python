# Write a program that contains a function that has one parameter, n, representing an integer
# greater than 0. The function should return n! (n factorial). Then write a main function that
# calls this
# function with the values 1 through 20, one at a time, printing the returned results. This is what
# your
# output should look like:
# 1
# 2
# 6
# 24
# 120
# 720
# 5040
# 40320
# 362880
# 36288002

def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        return n * factorial(n - 1)
    else:
        print("Enter valid positive number")


def main():
    for value in range(1, 21):
        print(factorial(value))


main()
