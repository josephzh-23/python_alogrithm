"""

Using k digits here wouldb e a lot better
Using a monotonic stack here

When we see an element x, if x > the last one in stack, stack.pop()
and then we add this element

if the string is "1432219"   k = 3
then remove string is "1219" as shown above here

remove the string 4,3, 2
"""

stack = [1, 2, 3, 4, 5]
print(stack[:-2])       # the above is for truncating elements as said


def removeKDigits(nums, k):
    stack = []
    for c in nums:
        while k > 0 and stack and stack[-1] > c:
            k-=1
            stack.pop()
        stack.append(c)


    stack = stack[:len(stack)-k]
    res = "".join(stack)
    return int(res)