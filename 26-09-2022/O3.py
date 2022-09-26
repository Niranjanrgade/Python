# Write a program that input a string and ask user to delete a given word from a string.

string_text = input("Enter a string: ")

input_word = input("Enter the word a from string to be deleted: ")

word_list = string_text.split(" ")

for word in word_list:
    if word == input_word:
        word_list.remove(word)

new_string = ''

print(' '.join(word_list))

for word in word_list:
    new_string += word + ' '

print(new_string)


