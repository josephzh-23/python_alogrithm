'''
This is the one where 1 open needs 2 close brackets here
- this makes a bit more sense here,




The implementation of the solution involves a greedy approach to satisfy the conditions for a balanced parentheses string, as mentioned earlier. The algorithm can be detailed as follows:

Initialize Two Counters:

 We have two counters ans and x,

numInsertionNeeded:
  where numInsertionNeeded keeps track of the number of insertions needed and
unMatchedOpenParenthesis:
   unMatchedOpenParentesis keeps track of the number of unmatched opening parentheses that are yet to be paired with a closing parentheses.


Handling Opening Parentheses '(': When we encounter an opening parenthesis,

  unMatchedOpenParenthsis+=1, as we need to find or insert two consecutive closing parentheses to balance it.

Handling Closing Parentheses ')':

if cur == ')':
    If the current character is a ')', we first check whether it forms a pair with the next character (i.e., if it is followed by another ')'). If yes, we increment i by 1 to skip the next character since we have a complete pair '))',

    and then we decrement unMatchedOpenParentesis.


If there is no ')' following the current one, we increment numInsertionNeeded as we need to insert an additional ')' to have a pair '))'.

We then check unMatchedOpenParentesis:

if unMatchedOpenParentesis is zero (meaning we have an excess of closing parentheses),
numInsertionNeeded+=1
 again to insert a '(' before the existing ')'.

 Otherwise, if unMatchedOpenParentesis is not zero, we simply decrement x.
Handle Unmatched Opening Parentheses: After the loop, if we still have unmatched opening parentheses (i.e., if x is greater than zero), it means we need to insert two ')' for each. We do this by adding x << 1 (which is equivalent to x * 2) to ans.

Returning the Result: Finally, the ans counter now contains the minimal number of insertions needed to balance the string according to the problem constraints, and we return this value.

The key points in this greedy algorithm are:

Efficiently keeping track of the number of parentheses we need to insert.
Balancing insertions only when necessary to fulfill the condition that each '(' is followed by two ')'.
Using bitwise shift x << 1 as a quick operation to double the x value, which is equivalent to adding two closing parentheses for every unmatched '(' at the end of the iteration.
By following this approach, we can guarantee the minimum number of insertions needed to achieve a balanced string.
'''


def min_insertions(self, s: str) -> int:

    # 'balance' keeps track of the balance of the parentheses
    # 'insertions_needed' will be the answer, representing the minimum insertions needed
    insertions_needed = balance = 0
    i, n = 0, len(s)  # 'i' is the current position, 'n' is the length of the string

    while i < n:  # Iterate through the string

        if s[i] == '(':  # If the current character is an opening parenthesis
            balance += 1  # Increase balance

            '''
            s[i] == ')'
            '''
        else:  # If the current character is a closing parenthesis
            # Check if there's a consecutive closing parenthesis
            if i < n - 1 and s[i + 1] == ')':
                i += 1  # Move to the next character as we've found a pair "))"

            else:
                # If a pair wasn't found, one insertion is needed
                insertions_needed += 1


            '''
             If there is no unmatched opening parenthesis
             '''
            if balance == 0:
                # We need an insertion for an opening parenthesis
                insertions_needed += 1
            else:
                # Otherwise, use one unmatched opening to balance a pair "))"
                balance -= 1
        i += 1  # Move to the next character

    # After processing the entire string, we might have unmatched opening parentheses
    # Each of these needs two insertions to be balanced (one opening parenthesis needs "))")
    insertions_needed += balance * 2

    return insertions_needed  # Return the total number of insertions needed