list_of_words = []
size = int(input("Enter the size of list: "))

for i in range(size):
    word = input("Enter word: ") 
    list_of_words.append(word) 

longest_word = ''
longest_word_size = 0


def find_longest_word(list1):
    global longest_word, longest_word_size
    for word_in_list in list1:
        if len(word_in_list) > longest_word_size:
            longest_word_size = len(word_in_list)
            longest_word = word_in_list
    
    print(f"The longest word is : {longest_word}")
    print(f"The longest word size is : {longest_word_size}")


find_longest_word(list_of_words)



