# A pangram is a sentence that contains all the letters of the English alphabet at least once, for
# example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to
# check a sentence to see if it is a pangram or not.

sentence = input("Enter the sentence which is to be checked for pangram: ")

sentence = sentence.lower()

alphabets = 'abcdefghijklmnopqrstuvwxyz'

alphabets_list = []

for alphabet in alphabets:
    alphabets_list += alphabet

letter = ''
list_of_letter_in_sentence = []

for index in range(len(sentence)):
    letter = sentence[index]
    list_of_letter_in_sentence += letter

sentence_contains_all_letters = False

for alphabet in alphabets_list:
    if alphabet not in list_of_letter_in_sentence:
        sentence_contains_all_letters = False
        break
    else:
        sentence_contains_all_letters = True

if sentence_contains_all_letters:
    print("It is a pangram.")
else:
    print("It is not pangram.")
