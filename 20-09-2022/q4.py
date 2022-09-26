num_str = input("Enter the number: ")
digit_places = len(num_str)
num = int(num_str)


def digit_to_word(digit_in_num):
    if digit_in_num == 0:
        return 'zero'
    elif digit_in_num == 1:
        return 'one'
    elif digit_in_num == 2:
        return 'two'
    elif digit_in_num == 3:
        return 'three'
    elif digit_in_num == 4:
        return 'four'
    elif digit_in_num == 5:
        return 'five'
    elif digit_in_num == 6:
        return 'six'
    elif digit_in_num == 7:
        return 'seven'
    elif digit_in_num == 8:
        return 'eight'
    elif digit_in_num == 9:
        return 'nine'


digit_list = []
for i in range(digit_places):
    digit = num % 10
    num = num // 10
    str_word = digit_to_word(digit)
    digit_list.append(str_word)


digit_list.reverse()
print(f"The digits in number are: {digit_list}")

