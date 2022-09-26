# An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is
# equal to the number itself.
# For example, 371 is an Armstrong number since 27+343+1 = 371.
# Write a program to find all Armstrong number in the range of 0 and 999

armstrong_list = []
for number in range(1000):
    first_digit = number // 100
    second_digit = (number // 10) % 10
    third_digit = number % 10

    if first_digit ** 3 + second_digit ** 3 + third_digit ** 3 == number:
        armstrong_list.append(number)

print(armstrong_list)
