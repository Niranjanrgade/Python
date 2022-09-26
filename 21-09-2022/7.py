# Write a program to sum all the values of a dictionary. 
# Hint dict1 = {‘key 1’: 200, ‘key 2’: 300} 
# Expected output Result: 500

dict1 = {'key 1': 200, 'key 2': 300} 

values = list(dict1.values())

sum_of_values = 0

for value in values:
    sum_of_values += value

print(sum_of_values)
