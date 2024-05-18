from typing import List

"""

The only difference between this and the first one is the first one is not cricular 
but this one is 
Let's take an example [1,5,7,9,6,8,3,2]
as we know we have to find the nearest greater element so 
#first approach we find the nearest greater to right
but as we also know that it is a circular array 


# so for that purpose we have to check for
 the elements in the starting of
 the array so we can first intially push all the elements in the stack 
 and we also know that stack is LIFO so we have to intially push all the elements in reverse order 


Example :  [1,5,7,9,6,8,3,2]
stack=     [2,3,8,6,9,7,5,1]
answer =   [-1,-1,-1,-1,-1,-1,-1,-1]
so for the value no.2 at index - 7
so we got from the stack as 1<=2 -- True
pop(1)
then , 5<=2 -- False
so add 5 into the answer array at the i index
answer =   [-1,-1,-1,-1,-1,-1,-1,5]
"""

def nextGreaterElements(nums: List[int]) -> List[int]:
    n = len(nums)
    ret = [-1] * n

    # reverse the elements here
    stack = nums[::-1]
    for i in range(n - 1, -1, -1):

        # get the greatest element in there
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        # if stack not empty, ther are no greater elements than those in the one in the stack
        if stack:
            ret[i] = stack[-1]
        stack.append(nums[i])
    print(ret)
    return ret


nextGreaterElements([1,2,3,4,3])
