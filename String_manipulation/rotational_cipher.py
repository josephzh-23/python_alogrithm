'''

And then here this is important here

'''


def getCipher(c, k):
    if c.isdigit():
        return chr(ord("0") + (ord(c) - ord("0") + k) % 10)
    if c.isalpha():
        if c.islower():
            return chr(ord("a") + (ord(c) - ord("a") + k) % 26)
        else:
            return chr(ord("A") + (ord(c) - ord("A") + k) % 26)

print(getCipher('c', 3))

def variantGiveCeaserCipher(s, k):
    res= ""

    for c in s:
        res += getCipher(c, k)
    return res
