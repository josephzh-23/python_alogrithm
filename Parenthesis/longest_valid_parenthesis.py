

'''
Uber interview problem with characters '(' and ')'
length of lognest valid

( () -> 2
) ()  () ) -> 4

TC: O(n)
SC: O(n)
'''
import string


def longestValidParen(str: string):

    maxi = 0
    map = {")": "("}
    stack = []

    curMax= 0
    # problem in here
    # sample ( ) how to know when you have one

    '''
    () () 2 
    () (  1     the value reset to 0 
    '''
    i = 0
    for c in str:
        if len(stack) == 0:
            stack.append(c)

        # already sth inside
        else:

            # this checks for matching

            if stack[-1] == c:
                curMax = 0

            elif stack[-1] == map[c]:
                stack.pop()
                curMax+=1
                maxi = max(curMax, maxi)

        i+=1
    print(maxi)
    # for each valid -> return 1
    #

longestValidParen('()()()((()()()()')
# this return 3
