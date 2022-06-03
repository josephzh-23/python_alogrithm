def isValidParenthesis(s):

    stack= []
    for c in s:
        if c in ["(", "{", "["]:
            # Push the element in the stack
            stack.append(c)

        elif c== ')' and stack and stack[-1] == '(':
            stack.pop()
        elif c== ')' and stack and stack[-1] == '[':
            stack.pop()
        elif c== ')' and stack and stack[-1] == '{':
            stack.pop()

        # sth is going on
        else:
            return False


    isStackEmpty = False

    if len(stack) ==0:
        isStackEmpty= True

    # if stack is empty, that means we have succeeded
    # in removing whatever we need to remove
    return isStackEmpty


print(isValidParenthesis("()"))