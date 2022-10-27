

# divide into 2 subsets A and B for packaging boxes

# A and B intersection null
# union A and B = original array
'''
Answer arr = [3, 7, 5, 6, 2]
returned value [5, 7] and [6, 7]
 sum
 find a condition for divdigin

 # can sort it first
 [2, 3, 5, 6, 7]
 start from back    13 the max

 13 > 10
 12 > 11
 10 <

 [1, 2, 2, 3, 4, 5]
 [4, 5]

 9 > 8      if it is then add to setA
 8 < 9
'''
def trial(arr):

    arr.sort()
    print(arr)
    # get the total sum first for each one
    totalSum = 0
    for num in arr:
        totalSum += num

    print(totalSum)
    arrA = []
    # use the ipointer and start fomr the back
    i = len(arr) -2
    j = len(arr) -1

    res = []

    # res always have the last value
    res.append(arr[j])

    # need to find the max first and then compare
    for num in arr:
        if i >=0:
            curSum = arr[j] + arr[i]
            remainSum = totalSum - curSum

            if curSum > remainSum:
                res.append(arr[i])
            i-= 1
            print('index val is ' ,i)
            print('cur sum is ',  curSum, " total sum", remainSum)
    return res

arr = [3, 7, 5, 6, 2]

res = trial(arr)
print(res)



