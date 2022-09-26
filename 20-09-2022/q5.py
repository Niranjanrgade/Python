size = int(input("Enter the n (quantity of) numbers: "))
list1 = []

for i in range(size):
    num = int(input("Enter the numbers: "))
    list1.append(num)

sum_of_numbers = 0

for num in list1:
    sum_of_numbers = sum_of_numbers + num

print(f"Sum of n numbers: {sum_of_numbers}")