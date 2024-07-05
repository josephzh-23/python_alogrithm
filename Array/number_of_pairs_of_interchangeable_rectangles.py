'''

Here what happens then?
'''


def numInterchangeables(rectangles):
    dict = {}
    res = 0
    for r in rectangles:
        width, height = r

        ratio = width // height

        # store the ratio
        if dict.get(ratio, 0) == 0:
            dict[ratio] = 1
        elif ratio !=0:
            res+=2

    print('res is', res)
    return res

numInterchangeables([[4, 5], [7, 8]])
