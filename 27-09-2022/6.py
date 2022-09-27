# Write a definition of a method count_now(places) to find and
# display those place names, in which there are more than 5 characters.
# For example : If the list places contains ["DELHI","LONDON","PARIS","NEW YORK","DUBAI"]
# The following should get displayed : LONDON NEW YORK

places = ["DELHI", "LONDON", "PARIS", "NEW YORK", "DUBAI"]


def count_now(places):
    for place in places:
        if len(place) > 5:
            print(place, end=' ')


count_now(places)

