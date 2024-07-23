from typing import List


''' 



Return this in the largest number possible here 
'''


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        current_value = 1
        lex_order_list = []

        # Generate n lexicographic numbers
        for _ in range(n):
            # Append current value to the result list
            lex_order_list.append(current_value)

            # If the current value times 10 is less than or equal to n,
            # then *10 will still give us a lexicographically smaller number
            if current_value * 10 <= n:
                current_value *= 10
            else:
                # If current_value * 10 is larger than n, we check:
                # If the current value is the end of the range (ends in 9)
                # or adding one to current value would exceed n,
                # we continuously divide current_value by 10 until it's not.
                while current_value % 10 == 9 or current_value + 1 > n:
                    current_value //= 10

                # Finally, we increment current_value by one to get the next valid number
                # in lexicographical order that is also less than or equal to n.
                current_value += 1

        # Return the list containing all n numbers in lexicographical order
        return lex_order_list
