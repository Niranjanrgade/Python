list_a = [1, 2, 3]
list_b = [0, 5, 2]


def overlapping(list1, list2):
    flag = False
    for i in list1:
        for j in list2:
            if i == j:
                flag = True
            else:
                pass
    return flag


print(overlapping(list_a, list_b))
