'''


605 very similar to asteroid collision problem

can place flowers in adjacent plots, meaning the flowers like in the following case will not work here
'''

flowerbed = [1,0,0,0,0,0, 1]; n = 2
def canPlaceFlowers(flowers, n):
    count = 0
    for i in range(1, len(flowers)):
        if flowers[i -1] == 0 and flowers[i] == 0 and flowers[i + 1] == 0:
            count +=1
            flowers[i] = 1
            if count == n:
                return True

    return False
print(canPlaceFlowers(flowerbed, n))











