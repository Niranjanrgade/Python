# Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go
# hanga salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan,
# Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a
# tired nude Maori","Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that
# punctuation, capitalization, and spacing are usually ignored.

phrase = input("Enter the phrase: ")

phrase = phrase.lower()

alphabets = 'abcdefghijklmnopqrstuvwxyz'


def clear_phrase(text):
    letter = ''
    cleared_phrase = ''
    for index_of_letter in range(len(text)):
        for alphabet in alphabets:
            letter = text[index_of_letter]
            if letter == alphabet:
                cleared_phrase += letter
    return cleared_phrase


phrase = clear_phrase(phrase)

reverse_phrase = phrase[::-1]

is_palindrome = False

for index in range(len(phrase)):
    if phrase[index] == reverse_phrase[index]:
        is_palindrome = True

print()

if is_palindrome:
    print("It is a palindrome.")
else:
    print("It is not palindrome.")
