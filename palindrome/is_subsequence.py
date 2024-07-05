'''

Once this is done then next thing comes up
'''


def isSubsequence(s, t):
    leftBound = s.length
    rightBound = t.length
    pLeft = 0
    pRight = 0
    while (pLeft < leftBound and pRight < rightBound):
        if s[pLeft] == t[pRight]:
            pLeft += 1

        pRight += 1

    return pLeft == leftBound
