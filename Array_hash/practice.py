

#

def kTopOccuringElems(arr, k):


    ans = []
    map = {}

    for num in arr:
        if num not in map:
            map[num] = 1
        else:
            map[num] +=1