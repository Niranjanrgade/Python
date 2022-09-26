# Write a program that display following output:
# SHIFT
# HIFTS
# IFTSH
# FTSHI
# TSHIF
# SHIFT

text = 'SHIFT'

for iterator in range(6):
    print(text[iterator:] + text[:iterator])
    
    