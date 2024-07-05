'''
Lower bound returns an index, ind, such that arr[ind] >= x(i.e. target element),

Upper bound:  the upper bound returns the
index of the first element that is greater than the target element i.e. arr[ind] > x.


 In this case we have to find the first element >= k,

 so every-time we find an element  >= to the element k
 , only than we update our ans to mid and make low= mid+1.

 Else we update high = mid-1.


'''

def upperBound(arr, target):
    low = 0; high = len(arr) - 1; ans = 0

    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] > target:
            ans = mid
            high = mid -1
        else:
            low= mid + 1
        print(mid)
    return ans

print(upperBound([2, 4, 6, 8, 8, 8, 11, 13], 8))

def lowerBound(arr, target):
    low = 0;
    high = len(arr) - 1;
    ans = 0

    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
        print(mid)
    return ans
# print(lowerBound([2, 4, 6, 8, 8, 8, 11, 13], 8))
