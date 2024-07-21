'''

A string containing * and then

- Non-star char to its left and remove the star itself here

- Keep t

'''

def removeStarFromLeft(s):
    stk = []
    for i, c in enumerate(s):
        stk.append(c)
        if c == '*':
            stk.pop()
            stk.pop()
    print(''.join(stk))


# s = 'leet**cod*e'
s = 'erase*****'
removeStarFromLeft(s)