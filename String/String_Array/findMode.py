def findMode(List):
    dict = {}
    count, itm = 0, ''
    for item in reversed(List):

        print('You are')
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return (itm)


cist = [2, 1, 2, 2, 1, 3]
print(findMode(cist))