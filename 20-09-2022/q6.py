list1 = ['a', 'aa', 'a'*3, 'a'*4, 'a'*5, 'a'*6, 'a'*7, 'a'*8, 'a'*9]
length = int(input("Enter the length for filter: "))


def filter_long_words(list_of_words, length_for_filter):
    for word in list_of_words:
        if len(word) > length_for_filter:
            print(word)


filter_long_words(list1, length)

