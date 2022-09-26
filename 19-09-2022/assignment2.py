list1 = [4, 5, 6, 7]


def swap():
    print(f"Before swapping: {list1}")
    temp = list1[0]
    list1[0] = list1[-1]
    list1[-1] = temp
    print(f"After swapping: {list1}")


swap()
