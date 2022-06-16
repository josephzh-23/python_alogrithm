


def reverseStringStack(str):

    # 'joseph'
    size = len(str)
    s = []
    res = []
    for i in range(size):
        s.append(str[i])

    for i in range(size):
        res.append(s.pop())

    return res

print(reverseStringStack("joseph"))