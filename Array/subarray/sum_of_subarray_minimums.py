'''


Sum of subarray minimums here

First, initialize two arrays, left as [-1, -1, -1, -1] and right as [4, 4, 4, 4]. The -1 indicates that we didn't find a previous smaller element yet, and 4 is used because it's the size of arr, indicating we haven't found the next smaller or equal element yet.


If we have
[3, 1, 2, 4]

Create a stack monotonically increasing stack to store the index of the next greater elements here
- and then that's it here

-
Iterate through arr from left to right:

i = 0, arr[i] = 3, stack is empty, so push 0 onto the stack.
i = 1, arr[i] = 1, stack top element is 3 (> 1), so pop 0. left[1] becomes the previous element, -1. Stack is empty, push 1.
i = 2, arr[i] = 2, stack top element is 1 (< 2), do nothing. Push 2 to the stack.
i = 3, arr[i] = 4, stack top element is 2 (< 4), do nothing. Push 3 to the stack.
After this loop, left becomes [-1, -1, 1, 2], and stack stk contains [1, 2, 3].



'''
from typing import List


def sumSubarrayMins(arr: List[int]) -> int:
    n = len(arr)  # Get the length of the input array
    left = [-1] * n  # Store the index of previous smaller element for each element in the array
    right = [n] * n  # Store the index of next smaller element for each element in the array
    stack = []  # Initialize an empty stack for indices

    # Form a monotonically increasing array here and that's step number 1 here
    for i, value in enumerate(arr):
        while stack and arr[stack[-1]] >= value:
            stack.pop()
        if stack:
            '''
            Example 
            3, 1, 2, 4
            
            when i = 2 
            arr[i]  =2 
            stack[-1] = 1 meaning index 1 
            left[2] = 1 
            
            meaning previous smaller element of left is 2 here 
            
            In the end stack will have 
            
            After this loop, left becomes [-1, -1, 1, 2], and stack stk contains [1, 2, 3].
            '''
            left[i] = stack[-1]  # Update left index if stack is not empty
        stack.append(i)  # Push the current index onto the stack
    print(stack)
    stack = []


    '''
     Example 
        3, 1, 2, 4
    Part 2 comes the right array 

    At i = 2 
    arr[i] = 2 
    stack[-1] = 4 
    
    Pop 3 
    
    i = 3, arr[i] = 4, stack is empty, push 3 onto the stack.
    i = 2, arr[i] = 2, stack top element is 4 (> 2), so pop 3. Push 2 onto the stack.
    i = 1, arr[i] = 1, stack top element is 2 (> 1), pop 2, right[1] is 2. Stack is now empty again, push 1.
    i = 0, arr[i] = 3, stack top element is 1 (< 3), so do nothing. Push 0 onto the stack.
    

    After this loop, right becomes [3, 2, 3, 3], and stack stk contains [1, 0].
    Meaning at 4, 
        At index 0, the nextGreater is 4 (meanning we couldn't find the nextGreater)
        At index 1, the nextGreater is at index 2 
        
    '''
    # Calculate the next less element for each element in the array, going backwards
    for i in range(n - 1, -1, -1):  # Start from end of the array and move backwards

        '''
        [3, 1, 2, 4] 
        
        Example
        at index 2
        arr[2] = 2
        stack[-1] = 3
        arr[3] > arr[2] 
        so we pop
        right[2] = 3
        '''
        while stack and arr[stack[-1]] > arr[i]:  # Similar stack operation but with strict inequality
            stack.pop()  # Pop elements while current element is smaller

            '''
            At this point the current element is bigger which is why we can then do
            right[i] = (the index of the next smaller element)
            '''
        if stack:
            right[i] = stack[-1]  # Update right index if stack is not empty
        stack.append(i)  # Push current index to the stack
    #
    print('currently the right is', right)
    mod = 10 ** 9 + 7  # Define modulus for the final result

    # Calculate the sum of all minimum subarray values with their respective frequencies
    # The frequency is the product of the lengths of subarrays to the left and right
    result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod


arr = [3, 1, 2, 4]
sumSubarrayMins(arr)