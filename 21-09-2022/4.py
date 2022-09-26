# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
# That is, double every consonant and place an occurrence of "o" in between.
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".

text = input("Enter the text which will translate into \"rövarspråket\": ")

text = text.lower()

rövarspråket = ''

for i in range(len(text)):
    consonant = ''
    if text[i] != 'a' and text[i] != 'e' and text[i] != 'i' and text[i] != 'o' and text[i] != 'u':
        consonant = text[i] + 'o' + text[i]
        rövarspråket += consonant
    else:
        rövarspråket += text[i]

rövarspråket = rövarspråket.replace(' o ', ' ')

print(rövarspråket)
