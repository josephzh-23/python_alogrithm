


def monotonicIncreasing(nums):
    stack = []
    result = []

    # Traverse the array
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

# Example usage:
nums = [3, 1, 4, 1, 5, 9, 2, 6]
result = monotonicIncreasing(nums)
print("Monotonic increasing stack:", result)




