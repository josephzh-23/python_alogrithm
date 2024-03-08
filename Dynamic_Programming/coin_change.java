package Dynamic_programming;

import java.util.Arrays;

/*
https://leetcode.com/problems/coin-change/
Basically break this into a subproblem
1. [1, 3, 4, 5] 		Amt = 7
min coin  should be 2, 	with [ 3 + 4]

At each position the decision is 1, 3, 4, 5
answer = Amount - num picked

[1, 3, 4, 5] 		Amt = 7
Use bottom up approach. Start from the bottom.
So check following,
dp[0] = 0		means what’s the min # of coins needed to sum to 0, is 0
dp[1] = 1		min# of coins to sum to 1

dp[2] = 2 = 1 + 1 = dp[1] + 1
dp[3] = can take 3 or [1 +2]
dp[4] = 1			// already have a 4 so only takes 1
dp[5] = 1				dp[6] = 2

So consider case for dp[7]
Option 1: at coin 6, add 1			mincost = 3?
dp[7] = 1+ dp[6] 	 this give you 3,since 1+ 2 = 3, not the min # of 						coins though

 */
class Solution15{
    public int coinChange(int[] coins, int amount){

        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;

        /*
        Want the fewest # of coins to make up the ith set,
        take different coins and get the results

        Loop thru the coin, and you get the
        if amount = 2

         */

        for (int i = 0; i <= amount; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (coins[j] <= i) {
                    dp[i] = Math.min(dp[i], 1 + dp[i - coins[j]]);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }

}