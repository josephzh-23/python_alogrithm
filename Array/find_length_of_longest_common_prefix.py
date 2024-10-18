'''

And on here you will get the question

# length of longest common prefix here then you have hte code

#Legnth of the longest common prefix


Input: arr1 = [1,10,100], arr2 = [1000]
Output: 3
Explanation: There are 3 pairs (arr1[i], arr2[j]):
- The longest common prefix of (1, 1000) is 1.
- The longest common prefix of (10, 1000) is 10.
- The longest common prefix of (100, 1000) is 100.
The longest common prefix is 100 with a length of 3.


Using the code above we have
'''


def longestCommonPrefix(self, arr1, arr2):
    arr1_prefixes = set()  # Set to store all prefixes from arr1

    # Step 1: Build all possible prefixes from arr1
    for val in arr1:
        while val not in arr1_prefixes and val > 0:
            # Insert current value as a prefix
            arr1_prefixes.add(val)
            # Generate the next shorter prefix by removing the last digit
            val //= 10


    longest_prefix = 0

    # Step 2: Check each number in arr2 for the longest matching prefix
    for val in arr2:
        while val not in arr1_prefixes and val > 0:
            # Reduce val by removing the last digit if not found in the prefix set
            val //= 10

        # that means a match is found here  and then
        if val > 0:
            # Length of the matched prefix using log10 to determine the number of digits
            longest_prefix = max(longest_prefix, len(str(val)))

    return longest_prefix

num1 = 1; num2 = 1000

# and that's only second of the problem that we have dealt with so far here
print(longestCommonPrefix(str(1), str(1000)))