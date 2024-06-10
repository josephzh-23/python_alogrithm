

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

        # When we get closing paren, it's also in the map
        if c in map:
            # this checks for for the matching bracket at the end
            if stack and stack[-1] == map[c]:
                print(c)
                stack.pop()

        # when we get an open bracket
        else:
            # print(c)
            stack.append(c)

    # only return true if stack empty
    return True if not stack else False

print(isValidParenthesis("()[]"))