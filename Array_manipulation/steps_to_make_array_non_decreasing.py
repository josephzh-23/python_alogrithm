

'''
remvoe all eleements nums[i] where nums[i- 1] > nums[i]
for all 0 < i < len(nums) here

Hints:
1. An element element will be removed if and only
if there exists a strictly greater element to the left of it in the array.

Using a dp structure here
2. we use a dp (dynamic programming) array to keep track of the
number of steps taken to remove the next smaller elements.

And then
3. When we hit an element that could cause the removal of other elements,
we need to calculate how many removal steps it took for the next-smallest elements
 and update it to the
 maximum of the current steps recorded plus one or the steps taken for that element already.

    - so this makes sure we have the max # of steps for each element here

    -

1.
Use a  stack to keep track of elem that need to be remvoed here


'''
from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # Initialize an empty stack to keep track of indices
        # that needs to be revmoed here
        stack = []

        '''
       Each dp[i] = # steps required to remove the elem at nums[i] due to a larger p
       preceding element here  
       

Steps: 
1. Iter thru the nums in reverse, at each i check if nums[i] can cause 
removal of elem in the stack here 

2. Once inside the loop 

topIndex = stk[-1]         # the one at the top here 
check if nums[i] >  nums[topIndex]
This means cna lean to sth ehre 

AN dhtne we just keep going here, dp[i] increase this by one here 

- and then we here even have more data here than before as said 

x
        
        '''
        steps_to_remove = [0] * len(nums)

        # Initialize the max_steps as 0, to store the maximum
        # number of steps needed to remove any element
        max_steps = 0

        # Iterate the nums list in reverse order
        for i in range(len(nums) - 1, -1, -1):


            '''
            Below is the one at the top 
            '''
            # While the stack is not empty and the current number is greater than
            # the top element of the stack
            while stack and nums[i] > nums[stack[-1]]:
                # Calculate the steps to remove the current number
                # It's either 1 step more than its last or the steps needed to remove
                # the number at the top of the stack, whichever is greater
                steps_to_remove[i] = max(steps_to_remove[i] + 1, steps_to_remove[stack.pop()])

            # Add the current index to the stack
            stack.append(i)

        # and then here pretty much solve the problem here
        # Return the maximum steps needed to remove an element from nums
        max_steps = max(steps_to_remove)
        return max_steps


'''


Using here what's the TC?

0. Using stack and popping and pushing here, each elem can lead to pushing an popping here 
from the stack at once here 

1. Seems like could lead to higher TC, but the popping and pushing happens at each step anyways 
so it's actulaly not too bad

2. 
1. And i think we have sth like the previously what we said was this here 
we would have 

SC: 
Using here would be an O(c)
- 
'''