'''
Since, the number of opening bracket ‘[‘ and closing bracket is same ‘]’,
The optimal approach is to balance two sets of brackets in one swap

3. For every two pairs of square brackets, a swap will make them balanced.

4. If number of unbalanced pairs are odd
    then one more swap is needed.
    (p + 1) // 2

5.


'''


# Python3 implementation for the above approach

# Function to balance the given bracket by swap
def balancedStringBySwapping(s):
    # To count the number of uunbalanced pairs
    unbalancedPair = 0;
    for i in range(len(s)):

        # if there is an opening bracket and
        # we encounter closing bracket then it will
        # decrement the count of unbalanced bracket.
        if (unbalancedPair > 0 and s[i] == ']'):

            unbalancedPair -= 1;

        # else it will increment unbalanced pair count
        elif (s[i] == '['):

            unbalancedPair += 1;

    return (unbalancedPair + 1) // 2;