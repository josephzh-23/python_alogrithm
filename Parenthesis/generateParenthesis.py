from typing import List


# The question

"""
Question, if n = 3, how many parenthesis combination can you generate?
well combined parenthesis can we generate


['((()))', '(()())', '(())()', '()(())', '()()()']
"""
def generateParethesis( n: int) -> List[str]:

    """only add open paren if # open < n
    - only add a closing paren if closed < open
 valid iif open == closed == n
    """

    stack = []
    res = []

    # openN # of open brackets, closedN # of closed brackets
    def backtrack(openN, closedN):

        # now here it's finished
        if openN == closedN == n:
            res.append("".join(stack))

        #for adding open parenthesis always do this first
        if openN < n:
            stack.append("(")

            '''
            if n = 3
            0  0 
            1  0 
            2  0 
            2  1
            2  2
            '''
            print(openN, closedN)
            backtrack(openN +1, closedN)

            # Here we need to pop each time since what we have is a global varialbe

            stack.pop()

        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN +1)

            # here popping the close parent added
            stack.pop()

    backtrack(0, 0)
    print(res)
    return res

generateParethesis(3)