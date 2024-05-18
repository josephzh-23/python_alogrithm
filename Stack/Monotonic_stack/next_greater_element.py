'''

First elem that's greater to the right of x here
1.
For each 0 <= i < nums1.length,
find the index j such that nums1[i] == nums2[j]
 and determine the next greater element of nums2[j] in nums2.

 2. Nums 2 subset of 1 here,
  nums1 = [4,1,2], nums2 = [1,3,4,2]

'''
from typing import List


def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    if not nums2:
        return None

    mapping = {}
    result = []
    stack = []
    stack.append(nums2[0])

    for i in range(1, len(nums2)):
        # if stack is not empty, then compare it's last element with nums2[i]
        while stack and nums2[i] > stack[-1]:

            # if the new element is greater than stack's top element, then add this to dictionary
            '''
      based on the input here, if nums2 = [1, 3, 4, 2]
      our map would become [{1: 3,}, {3: 4}, {4: -1}, {2: -1}]
      
            '''
            mapping[stack[-1]] = nums2[i]

            stack.pop()  # since we found a pair for the top element, remove it.
        # add the element nums2[i] to the stack because we need to find a number greater than this
        stack.append(nums2[i])
    # if there are elements in the stack for which we didn't find a greater number, map them to -1
    for element in stack:
        mapping[element] = -1

    '''
    [{1: 3,}, {3: 4}, {4: -1}, {2: -1}]
    and then you check the mapping for nums1 value here and then compare 
    '''
    for i in range(len(nums1)):
        result.append(mapping[nums1[i]])
    return result
