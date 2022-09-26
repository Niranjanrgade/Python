num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print()


def swap(p1, p2):
    print("Before swap: ")
    print(f"First number: {p1}")
    print(f"Second number: {p2}")
    temp = p1
    p1 = p2
    p2 = temp
    print()
    print("After swap: ")
    print(f"First number: {p1}")
    print(f"Second number: {p2}")


swap(num1, num2)
