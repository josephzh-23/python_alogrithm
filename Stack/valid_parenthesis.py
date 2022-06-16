

'''
)  (   we want to make sure that ) matches (
        ] matches [

TC : O(n)
'''
def isValidParenthesis(s: str) -> bool:
    map = {")": "(", "]": "[", "}": "{"}
    stack = []

    # check if c is in the key
    for c in s:

        # When we get closing paren, we pop
        # what's already in theres
        if c in map:
            # if we get open
            if stack and stack[-1] == map[c]:
                # print(stack[-1])
                stack.pop()

        # when we get an open bracket
        else:
            print(c)
            stack.append(c)

    # only return true if stack empty
    return True if not stack else False

print(isValidParenthesis("()[]"))