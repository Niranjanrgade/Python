# Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# A. Find out how many students are in the list
# B. Change Lisa’s favourite colour
# C. Remove 'Jenny' and her favourite colour
# D. Sort and print students and their favourite colours alphabetically by name

people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}

print(f"Number of people: {len(people.keys())}")

favorite_colour = input("Enter Lisa's favorite colour: ") 
people['Lisa'] = favorite_colour
print(f"Lisa's favorite colour: {people['Lisa']}")

people.pop('Jenny')
print(people)

peoples_list = list(people.keys())
peoples_list.sort()

for index in range(len(peoples_list)):
    print(f"{peoples_list[index]} : {people[peoples_list[index]]}")
   