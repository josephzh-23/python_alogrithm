'''
Number here we can reverse the array here s

[10, 2]



1. Use a custom function here
2. Decides which combination (either a + b or b + a) compares
gives a bigger answer

3. Get rid of leading 0 here
'''


def largestNumber(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    stack = []
    result = []

    for num in nums:
        # While stack is not empty AND top of stack is more than the current element
        while stack and stack[-1] > num:
            # Pop the top element from the stack
            stack.pop()
        # Push the current element into the stack
        stack.append(num)

    # Construct the result array from the stack
    while stack:
        result.insert(0, stack.pop())

    return result


# a custom sorter here, can be used
def compareNumbers(self, a: str, b: str) -> int:
    # Custom comparator for sorting:
    # If the concatenation of a before b is less than b before a,
    # then we say a is "greater than" b in terms of the custom sorting.
    # That is, return -1 to indicate a should come before b.
    if a + b < b + a:
        return 1
    else:
        return -1


print(largestNumber([3, 30, 34, 5, 9]))












