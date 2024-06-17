'''

Given 2 integer arrays nums1 and nums2 sorted in non decrasing

an integer k one elem from first and 1 from 2nd here

-

'''
from Heap.max_heap import MinHeap


def solution(nums1, nums2, k):
    min = MinHeap()
    #store the results here
    ans = []
    m, n= len(nums1), len(nums2)

    ''' 
    Need to store 3 things here 
    1.  the pair's sum, 
    2. 1st elem index in nums1
    2.  and the second element's index in nums2.
    
    the indexes of each array here 
    '''

    visited = set()
    visited.add((0,0))

    # the first one here alwys the smallest which makes sense
    min.push((nums1[0] + nums2[0], (0, 0)))
    while min and k > 0:
        # gauranted the smallest pair
        val,(i, j) = min.pop()
        p = min.pop()

        ans.append(p)
        k-=1
        '''
        Check if there's a next element in 
        nums2 that can be paired with the same nums1 element. If so, add this new pair to the heap so that it can be considered in the next iteration.
        '''
        if i + 1 < m and (i + 1, j) not in visited:
            min.push((nums1[i + 1] + nums2[j], (i + 1, j)))
            visited.add((i + 1, j))

        if j + 1 < n and (i, j + 1) not in visited:
            min.push((nums1[i] + nums2[j + 1], (i , j + 1)))
            visited.add((i, j + 1))
        k-=1
    return ans