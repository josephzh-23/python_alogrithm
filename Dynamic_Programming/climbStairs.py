


# This is an interesting problem where

'''
Here if n = 5, then

0   1   2   3   4   5
8   5   3   2   1   1
               one  two
    Notice at 1:
From 1 to 5, there r 5 ways, which = 3 + 2
the same as the sum of previous 2 values
'''

# We will keep u
# n would be deciding factor here

def climbStairs(n):

    dp = [None] *(n+1)

    # Acting as pointer 0 and 1
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(" there r" +str(climbStairs(4))+ "ways to climb the stairs")





