'''


s = "abbaca"
b
stack = ab

'''



def removeAllAdjacentDuplicates(string):
    s = []
    for c in string:
        if s:
            if c == s[-1]:
                s.pop()
            else:
                s.append(c)
        else:
            s.append(c)
    return s


removeAllAdjacentDuplicates("abbaca")