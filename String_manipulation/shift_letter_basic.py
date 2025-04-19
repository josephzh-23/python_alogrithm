


'''

This is not actually the shift letter problem in leetcode but rather the
how to shift letters here

The basic shifting in python happens like this
chr(ord(char) - n)

chr : converts things back to a character
-97 % 26
make sure this is actually modulus

Basically 97 is ord(a)
'''


def shiftLetters(letters, n):
    res = ''
    for char in letters:
        res +=chr((ord(char) - 97 - n) % 26 + 97)

    print(res)

shiftLetters("abc", 3)