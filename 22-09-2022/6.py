# Write a Python program to read the admission number and names of 10 students from the
# keyboard. Create a dictionary of these admission number and names and then display them
# on the screen

student_dictionary = {}

for index in range(10):
    admission_number = input("Enter the admission number: ")
    name = input("Enter the names: ")
    student_dictionary[admission_number] = name

print(student_dictionary)
