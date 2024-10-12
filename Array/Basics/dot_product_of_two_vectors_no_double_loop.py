'''
Input:

nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
A sparse vector has mostly 0 values here
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

'''
from collections import defaultdict
from typing import List


# just for testing
def testRun(nums):
    for i, n in enumerate(nums):
        print('index is ', i, 'and vlaue is', n)


class SparseVector:
    def __init__(s, nums):
        s.nonzeros = {}

        # Return the dotProduct of two sparse vectors instances here
        # and then here we have
        '''
        
        Approach:
        Store non-zero values and their corresponding indices in a dictioanry

        Any index not present here will then correspond to a value 0 in the input array here 
        {index, value}
         [[1, 0, 0, 2, 3], [0, 3, 0, 4, 0]]
        # so first one we have is [1, 0, 0, 2, 3] 
        
        {0: 1}  {3: 2} , {3, 3} {1: 3}, {2: 4} 
        '''
        for i, n in enumerate(nums):
            if n != 0:
                s.nonzeros[i] = n

    # and then here we have the code vb
    def dotProduct(s, vec: 'SparseVector'):
        res = 0

        # iterate through each non - zero element in this sparsevector

        # update the dot product if the corresponding index has a non-zero value in the other vector
        for i, n in s.nonzeros.items():
            if i in vec.nonzeros:
                res += n * vec.nonzeros[i]
        return res


nums = [[1, 0, 0, 2, 3], [0, 3, 0, 4, 0]]
v = SparseVector([1, 0, 0, 2, 3])
v2 = SparseVector([0, 3, 0, 4, 0])
print(v.dotProduct(v2))
