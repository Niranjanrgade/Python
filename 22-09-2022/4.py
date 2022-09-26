# Write a program in Python to find out the frequency of each number in stored in a list
# using a python dictionary.
# Example
# List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]
# Output ={1: 1, 2:2,3:1,4:4,5:1,6:2,7:7,23:1}

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 6, 2, 4, 2, 5, 23, 6, 4]

dict_a = {}
for num in list1:
    count = dict_a.get(num)
    print(count)
    if count == None:
        dict_a[num] = 1
    else:
        dict_a[num] = count + 1

print(dict_a)
