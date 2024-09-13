'''
The question is titled

Maximize the minimum difference between any element pair by
selecting K elements from given Array

Can be done with binary search here
This will be in playground here

Input: N = 4, K = 3, arr = [2, 6, 2, 5]
Output: 1
Explanation: 3 elements out of 4 elements are to be
 selected with a minimum difference as large as possible.

 Selecting 2, 2, 5 will result in minimum difference as 0.
 Selecting 2, 5, 6 will result in minimum difference as 6-5=1

 How to solve this porblem ?

 1. Use binary search here, sort the array

 Helper function is used to check if selection of

 K elements is possible with minimum difference greater than
  dif calculated in previous iteration.
  If possible then true is returned or else false is returned.


'''

'''
# Python 3 implementation for the above approach

# To check if selection of K elements
# is possible such that difference
# between them is greater than dif
'''


def isPossibleToSelect(arr, N,
                       dif, K):
    # Selecting first element in the
    # sorted array
    count = 1

    '''
     prev is the previously selected element initially at index 0 as
    first element is already selected

    And then here it will make things worse 
    '''
    prev = arr[0]

    # Check if selection of K-1 elements
    # from array with a minimum
    # difference of dif is possible
    for i in range(1, N):
        '''
        If the current element is
         at least dif difference apart
         from the  previously selected
         element then select the current
         element and increase the count
         '''
        if arr[i] >= (prev + dif):
            count += 1
            '''
             If selection of K elements
             with a min difference of dif
             is possible then return true
             '''
            if count == K:
                return True

            '''
             Prev will become current
             element for the next iteration
            '''
            prev = arr[i]
    # If selection of K elements with minimum
    # difference of dif is not possible
    # then return false
    return False


def binarySearch(arr, left,
                 right, K, N):
    # Minimum largest difference
    # possible is 1
    ans = 1
    while (left <= right):
        dif = left + (right - left) // 2

        # Check if selection of K elements
        # is possible with a minimum
        # difference of dif
        if (isPossibleToSelect(arr, N, dif, K)):

            # If dif is greater than
            # previous ans we update ans
            ans = max(ans, dif)

            # Continue to search for better
            # answer. Try finding greater dif
            left = dif + 1

        # K elements cannot be selected
        else:
            right = dif - 1

    return ans


# Driver code
if __name__ == "__main__":
    N = 7
    K = 4
    arr = [1, 4, 9, 0, 2, 13, 3]

    # arr should be in a sorted order
    arr.sort()

    print(binarySearch(arr, 0, arr[N - 1], K, N)
          )

    # This code is contributed by ukasp.