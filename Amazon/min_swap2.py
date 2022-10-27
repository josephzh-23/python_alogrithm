

'''
the above
2   3   1   5   4   6
0   1   2   3   4   5

so 2 should be at 2, 3 should be at 4
  2 swaps   [2, 3, 1]
  1 swap [5, 4]
'''
def minSwap(arr):

    minSwap, idx, temp = 0, 0, 0
    while idx< len(arr):

        # the number not at the right position
        # so arr[2] != 3
        # then we need to do the swap
        if(arr[idx]!=(idx+1)):
            print(arr[idx])

            # this is how to do the swap
            temp = arr[idx]

            # arr[2] = arr[1]
            arr[idx] = arr[arr[idx] -1 ]

            # arr[1] = arr[2]
            arr[temp-1] = temp
            minSwap+=1
        else:
            idx+=1
    print(minSwap)
    return minSwap

arr = [2, 3, 1, 5, 4, 6]
print(minSwap(arr))