'''

Example Walkthrough
Let's use a small example to illustrate the solution approach. Suppose we have two strings str1 = "abab" and str2 = "ab".

We need to find the largest string x that can divide both str1 and str2.

Check for Compatibility: We first check if concatenating str1 with str2 is equal to str2 concatenated with str1.

str1 + str2 = "abab" + "ab" = "ababab"
str2 + str1 = "ab" + "abab" = "ababab"

Above is step 1 here

Since str1 + str2 is equal to str2 + str1, the two strings are compatible, and therefore, it's possible they have a common divisor string.

Find Length of the Common Divisor: Next, we find the greatest common divisor of the lengths of str1 (4) and str2 (2).

gcd(4, 2) = 2
The gcd tells us that the length of the largest string that
possibly divides both str1 and str2 is 2.

Extract the Common Divisor String: Since the gcd is 2,
 we take the first 2 characters from str1 to form our largest divisor string x.

str1[:2] = "ab"
So, "ab" is the string we expect to divide both str1 and str2. To verify, we can see that:

str1 divided by "ab" is "abab" / "ab" = "ab", which is the repetition of "ab" twice.
str2 divided by "ab" is "ab" / "ab" = "", which is the repetition of "ab" once.
The largest string that can divide both str1 and str2 is "ab", which matches our result from the solution approach. The solution is elegant and efficient, leveraging simple concatenation and the mathematical concept of greatest common divisor to determine the existence and length of a common divisor string.

'''
from math import gcd


def gcdOfStrings(self, str1: str, str2: str) -> str:
    # Check if the concatenation of the two strings in different order results in the same string.
    # This is required as the strings should be made of the same substrings for them to have a common divisor.
    if str1 + str2 != str2 + str1:
        # If they don't form the same string when concatenated in different orders,
        # there is no common divisor string and hence return an empty string.
        return ''

    # Find the gcd of the lengths of the two strings.
    # The gcd of the lengths will give us the maximum length the common divisor string can have.

    # the gcd function is quite special as mentioend here
    length_gcd = gcd(len(str1), len(str2))

    # Return the substring from 0 to length_gcd from the first string,
    # which is the greatest common divisor string.
    return str1[:length_gcd]
