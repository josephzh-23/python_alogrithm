

'''
Uber interview problem with characters '(' and ')'
length of lognest valid

( () -> 2
) ()  () ) -> 4

TC: O(n)
SC: O(n)

Instead of finding every possible string and checking its validity, we can make use of a stack while scanning the given string to:

Check if the string scanned so far is valid.

Push -1 first onto the stack here

2. For every ( encountered, push ( unto stack here

3. For every ), pop the top most element here,

    diff = curElemIndex - topElemOnStack


Find the length of the longest valid string.
In order to do so, we start by pushing −1 onto the stack. For every ‘(’ encountered, we push its index onto the stack.

For every ‘)’ encountered, we pop the topmost element. Then, the length of the currently encountered valid string of parentheses will be the difference between the current element's index and the top element of the stack.

If, while popping the element, the stack becomes empty, we will push the current element's index onto the stack. In this way, we can continue to calculate the length of the valid substrings and return the length of the longest valid string at the end.

See this example for a better understanding.



'''
import string

'''
If open push the index here, 
For input: "(()())", the stack manipulation would look like this:

Initial: stack = [-1]
Index 0: Push index of '(', so stack = [-1, 0]

Index 1: Push index of '(', so stack = [-1, 0, 1]

(( ) ())
   i 
   
Index 2: Pop (matching ')' with '('), so stack = [-1, 0] and max_len = 2

Index 3: Push index of '(', so stack = [-1, 0, 3]

Index 4: Pop (matching ')' with '('), so stack = [-1, 0] and max_len = 4
Index 5: Pop (matching ')' with '('), so stack = [-1] and max_len = 6
After the loop, max_len is 6, which is the correct length of the longest valid substring.

'''
def longestValidParentheses(self, s: str) -> int:
    stack = [-1]
    max_len = 0

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len

'''
Below supposedly give 4 here 
'''
longestValidParentheses(")()())")
# this return 3
