



'''

1. a.end < b.start
2. b.end < a.start
3. there is overlap and overlap >= duration
4. there is overlap and the overlap < duration
'''
slotsA = [[6, 8], [10, 18], [20, 50], [60, 120], [140, 210]]
slotsB = [[0,15], [60, 70], [] , [] , []]
def checkOverlap(list1, list2):

    i = 0
    sizeOfLen = len(slotsA) - 1
    while i<= sizeOfLen:
        a = list1[i]
        b = list2[i]

        # 1st 2 cases no overlap as indicated
        if a[1] < b[0] or b[0] < a[0]:
            print('no overlap')
        else:
            print('overlap')
        i+=1
# and then using t his we could have a better result then what we had before


slotsA = [[6, 8], [10, 18], [20, 50], [60, 120], [140, 210]]
slotsB = [[0,15], [60, 70], [22, 32], [22, 32], [22, 32]]
checkOverlap(slotsA, slotsB)


