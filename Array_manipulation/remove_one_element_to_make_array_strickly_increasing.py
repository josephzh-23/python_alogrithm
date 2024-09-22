


'''
Using this here
if can be made strickly increasing here after just 1 element here

-
'''


def monotonicIncreasing(nums):
    stack = []
    result = []
    canBeMade = True
    # Traverse the array
    for num in nums:
        # While stack is not empty AND top of stack is more than the current element
        while stack and stack[-1] > num:
            # Pop the top element from the stack

            canBeMade= False
            stack.pop()
        # Push the current element into the stack
        stack.append(num)
    print(canBeMade)
    # Construct the result array from the stack
    while stack:
        result.insert(0, stack.pop())
    print('the result here is ', result)
    return result


# nums = [1, 2, 10, 5, 7]
# monotonicIncreasing(nums)

