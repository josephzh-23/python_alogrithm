

'''
1. Use a depth to keep track here
2. When we encounter an opening parenthesis '(',
    we are going deeper into a level of nesting, so we increase d by 1.

3. When we see ')'
    come out by 1 here

4. We check if the previous character (s[i - 1])
        was an opening parenthesis '('. If it was, then we have found a "()" pair.

5. Each depth doubles the level here

6.
'''
    # for each valid -> return 1


def scoreOfParentheses(self, s: str) -> int:


    # Initialize the score and the current depth of the parentheses.
    score = current_depth = 0

    # Enumerate over the string to process each character along with its index.
    for index, char in enumerate(s):
        if char == '(':  # If the character is an opening parenthesis,
            current_depth += 1  # increase the depth.
        else:  # If it's a closing parenthesis,
            current_depth -= 1  # decrease the depth.
            # If the previous character was an opening parenthesis,
            # it's a pair "()". Add 2^depth to the score.
            if s[index - 1] == '(':
                score += 1 << current_depth

    # Return the final computed score.
    return score