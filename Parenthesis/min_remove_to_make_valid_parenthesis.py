'''

In the first pass, we iterate over the string from left to right,

ignoring any characters that are not parentheses.

 We only add parentheses to the stack if they maintain the balance,
 but we increment or decrement the counting variable x based on whether we encounter an opening '(' or a closing ')'.
 This ensures we don't add any extra closing parentheses.


However after 1st pass,



the task is to remove the min # of invalid parenthesis here
'''

def minRemoveToMakeValid( s: str) -> str:
    # Stack to keep track of characters that lead to a valid string
    stack = []

    # Counter to track the balance of parentheses
    open_count = 0


    # First pass to remove invalid closing parentheses
    for char in s:

        # If a closing parenthesis is encountered with no matching open, skip it
        # skip the unbalanced ) here
        if char == ')' and open_count == 0:
            continue
        # If an opening parenthesis is found, increment the open count
        if char == '(':
            open_count += 1

        # If a closing parenthesis is found and there is a matching open, decrement the open count
        elif char == ')':
            open_count -= 1
        # Add the character to the stack as it's part of valid substring so far
        stack.append(char)

    # Reset the open counter for the second pass
    open_count = 0
    # List to store the characters for the final answer
    answer = []


    # lee(t(c)o)de

    print("here string is ", stack)
    # Second pass to remove invalid opening parentheses; process characters in reverse
    for char in reversed(stack):

        # If an opening parenthesis is encountered with no matching close, skip it
        if char == '(' and open_count == 0:
            continue

        # If a closing parenthesis is found, increment the open count
        if char == ')':
            open_count += 1
        # If an opening parenthesis is found and there is a matching close, decrement the open count
        elif char == '(':
            open_count -= 1
        # Add the character to the answer as it is part of a valid substring
        answer.append(char)

    print("answer is", answer)

    # The characters in answer are in reverse order, reverse them back to the correct order
    return ''.join(reversed(answer))

s = "lee(t(c)o)de)"
minRemoveToMakeValid(s)