"""
And as said it will be

Example if you have "ace" and "abcde", the longest ocmmon sequence will then
be "ace" even though they are not consecutive
We will use a 2d grid here

The way to do this
The matrix would then look like the following at the top

    a   c    e
a   3
b   2
c       2
d           1
e           1

Say we find 1 at (e, e), and then we traverse back up to (d, e),
add the 1 to it
    At (c,c)    add another 1, so this becomes 2
    Then go back to (a, a)      add another 1 to make it 3

Basically if there is no match
   # if there is no match, we add the max of the
            # 2 values to the right and below the current cell

We usually start from teh bottom right corner and then work our way up to
now. And that's it, go diagnoal back up if there is a match

And then


"""
def longestCommonSubSequence(s, text1, text2):
    dp = [[0 for j in range(len(text2+ 1))] for i in range (len(text1) +1)]

    # start at the bottom right matrix and work way up
    for i in range(len(text1)-1, -1, -1):
        for j in range(len(text2) -1, -1, -1):

            # if there is a match
            if text1[i] == text2[j]:

                                # already a diagnoal value that exists
                dp[i][j] = 1 + dp[i+1][j+1]

            # if there is no match, we add the max of the
            # 2 values to the right and below the current cell
            # and that's it
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])
    return dp[0][0]

# And then that's it