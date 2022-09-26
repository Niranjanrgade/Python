# Write a program in Python to remove repetitive items from a list. 
# Hint Given num = [2,3,4,5,2,6,3,2] 
# Expected output Result: [2, 3, 4, 5, 6] 

size = int(input("The number of items in list: "))
list_of_items = []

for index in range(size):
    item = int(input("Enter item: "))
    list_of_items.append(item)

list_of_unique_items = []

for index in range(len(list_of_items)):
    if list_of_items[index] not in list_of_unique_items:
        list_of_unique_items.append(list_of_items[index])

print(list_of_unique_items)
