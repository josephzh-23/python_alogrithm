package Dynamic_programming;

import static java.lang.Math.min;

public class minPathSum {

    public int minPathSum(int[][] grid){
        int rows = grid.length;
        int cols = grid[0].length;
        if(grid == null || grid.length ==0){
            return 0;
        }
        int[][] dp = new int[grid.length][grid[0].length];
        // Fill the first row here

        for(int i = 1; i< dp.length; i++){
            dp[0][i] = dp[0][i-1] + grid[0][i];
        }
        // Fill first col
        for(int i = 1; i< dp[0].length; i++){
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        // Now fill the rest of the cell
        for(int i=1 ; i< rows; i++){
            for(int j = 1; j< cols; j++){
                dp[i][j] = grid[i][j] + min(dp[i-1][j],
                        dp[i][j-1]);
            }
        }
        return dp[rows-1][cols-1];
    }
}
