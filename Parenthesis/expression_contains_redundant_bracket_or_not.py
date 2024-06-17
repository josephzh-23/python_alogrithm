'''
Given a set check to see if it contains extra or not here
Example we can have

exp = (a + b + (c + d))
Output : no

No redundant open bracket,

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

                # remove from stack if seen ti already
                stack.pop()

        # when we get an open bracket
        else:
            if not c.isalpha() and c != '+' and c != '-' and c!= '*' and c!= '/':
                # print(c)
                stack.append(c)
    print(stack)
    # only return true if stack empty
    return True if not stack else False

print(isValidParenthesis("(a+b+(c+d))"))









