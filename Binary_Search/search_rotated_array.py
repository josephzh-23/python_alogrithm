from typing import List

'''
We will use the solution from tech dose
There r 2 cases, stricly increasing and strictly decreaseing

   Steps
   3 cases: 
        
       1. Compare the target with last value on that row    matrix[row][-1]
       2. Compare first value on row        matrix[row][0]
       
       Then inside that row 
       3. 


'''
def searchRotated(nums, tar):
    n = len(nums)
    l, r = 0, n-1
    mid = 0

    # as with most left and right pointers
    while l <r:
        mid = (l+r)//2
        if nums[mid] == tar:
            return mid

        # increaseing trends on the left  3 4 5 1  2
        #                                   l m    r
        elif nums[mid] > nums[l]:

            #this means on the left
            if nums[l]< tar< nums[mid]:
                r = mid-1
            else:
                l = mid + 1
                # the other case where the left side is not uniformly increaing
                '''
                  4  5   6  7  8  0   1  2
                               l  m      r
                '''
        else:
            if nums[mid] < tar < nums[r]:
                l = mid +1
            else:
                r = mid -1

    return -1

nums = [3 ,4, 5, 0, 1, 2]
print(searchRotated(nums, 4))



