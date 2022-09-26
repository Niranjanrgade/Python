def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    elif num == 1 or num == 0:
        return 1


for i in range(11):
    print(f"Factorial of {i} is {factorial(i)}")
