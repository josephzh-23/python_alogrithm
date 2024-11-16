'''

Let's do it in a way that this makes sense here
'''
from typing import List

'''
And then to keep going here we have the code 

'''


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    # Initialize index to track the position in the 'popped' sequence
    pop_index = 0

    # Initialize an empty list to simulate stack operations
    stack = []

    # Iterate through each value in the 'pushed' sequence
    for value in pushed:
        # Push the current value onto the stack
        stack.append(value)
        '''
        pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
        
        4 == 4 in this case
        
        '''

        print("stack is currently, ", stack)
        # Check if the top of the stack matches the current value in 'popped'
        # If it does, pop from the stack and advance the index in 'popped'
        while stack and stack[-1] == popped[pop_index]:

            '''
            1st
                Stack                   popped_index 
                come here [1, 2, 3, 4]  0
            
                come here [1, 2, 3, 5]  1
                
                come here [1, 2, 3]     2
                come here [1, 2]       3
                
            '''
            print("come here", stack, pop_index)
            stack.pop()
            pop_index += 1

    # If the pop_index is equal to the length of 'pushed', all elements were popped
    # in the correct order, hence we return True. Otherwise, return False.
    return pop_index == len(pushed)

validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1])