package Dynamic_programming

// Java Solution

/*
OC: O(n^2)
Longest palindromic substring

a

Video by tech dose may need to check out the video for better
representation
substr(string, i, j)
means the string from i to j		if i==j, then reference 1 letter from stirng

2. The table stored the true or false, it's a table of true or false
So if palind[i] [j] = true		that means from i to j, it’s a palindrome


substring[0][0] = 1	 1 means it's palindrome
substring[1][1] = 1
substring[2][2] = 1

when it's not palindrome put 0
And the way to check check if s[i] == s[i-1]
if it is they are palindrome

substring[0][1] = ab		false
substring[1][2] = ba		false
since these are true already no need to calculate again.
 */
/*
table[i][j]     means from i to j
At table[1][0],
if it's value

Check this out      Need to fill the table first
A few conditions for sth to be palindrome
if i = start,   j = end
Check boundary elem first
Take abcba  if s[i] = s[j]          'abcba' the 2 as
palindrome if the s[i+1][j-1] == 1      'bcb'

 */

// Java Solution
object LongestPalinSubstring {
    // A utility function to print
    // a substring str[low..high]
    fun printSubStr(
            str: String, low: Int, high: Int) {

        println(
                str.substring(
                        low, high + 1))
    }

    // This function prints the longest
    // palindrome substring of str[].
    // It also returns the length of the
    // longest palindrome
    fun longestPalSubstr(str: String): Int {
        // get length of input string
        val n = str.length

        // [i][j] means from i to j

        // table[i][j] will be 0 (or false) if
        // substring str[i..j] is not palindrome.
        // meaning from i to j is not palindrome
        // Else table[i][j] will be true
        val table = Array(n) { BooleanArray(n) }

        // All substrings of length 1 are palindromes
        var maxLength = 1
        for (i in 0 until n) table[i][i] = true

        // Condition 1
        // check for sub-string of length 2.
        // This checks for consecutive string #1
        var startIdx = 0
        // O(n)
        for (i in 0 until n - 1) {
            if (str[i] == str[i + 1]) {
                table[i][i + 1] = true
                startIdx = i
                maxLength = 2
            }
        }

        // Check for lengths greater than 2.
        // k is length of substring
        for (k in 3..n) {
            print("k is $k")
            // Fix the starting index
            for (i in 0 until n - k + 1) {
                // Get the ending index of substring from
                // starting index i and length k
                val j = i + k - 1

                // checking for sub-string from ith index to
                // jth index iff str.charAt(i+1) to
                // str.charAt(j-1) is a palindrome

                // This can be explained with above where
                // abbba    str[i] == str[j]    check boundary
                // str[i+1] == str[j-1]     check non-boundary
                if (table[i + 1][j - 1]
                        && str[i] == str[j]) {
                    table[i][j] = true
                    if (k > maxLength) {
                        startIdx = i
                        maxLength = k
                    }
                }
            }
        }
        print("Longest palindrome substring is; ")
        printSubStr(str, startIdx,
                startIdx + maxLength - 1)

        // return length of LPS
        return maxLength
    }

    // Driver program to test above functions
    @JvmStatic
    fun main(args: Array<String>) {
        val str = "forgeeksskeegfor"
        println("Length is: " + longestPalSubstr(str))
    }
}

// This code is contributed by Sumit Ghosh