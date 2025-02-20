"""
8. Use for-loops to print out every 3-letter word that:
starts with one of these letters: c, t, b
has one of these letters in the middle: a, o
ends with one of these letters: p, t, n

(This should print out 18 words in total)
"""

first = "ctb"
middle = "ao"
last = "ptn"


for letter_1 in first:
    one_letter = letter_1
    for letter_2 in middle:
        two_letters = one_letter+letter_2
        for letter_3 in last:
            three_letters = two_letters+letter_3
            print(three_letters)