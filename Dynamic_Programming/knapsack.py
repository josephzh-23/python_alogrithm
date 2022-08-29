'''

    Given weights and values of n items, put these items in a knapsack of capacity W
 to get the maximum total value in the knapsack.

 In other words, given two integer arrays val[0..n-1] and wt[0..n-1]
 which represent values and weights associated with n items respectively.

The problem statmeent here:
    Also given an integer W which represents knapsack capacity,
 find out the maximum value subset of val[]
 such that sum of the weights of this subset is smaller than or equal to W
'''

# and then you keep going

'''
Check the row above 

    0   
   So the trick is we include an elem if the val[i] (current value) and the 
   val[i-1] the (value in the row above) differs
   
   the idea: 2 values differ, the current row must have had the item included, 
   otherwise the value wouldn't have changed
   
   The idea: .
   
   The knapsack problem 
   
   
'''
# c stands for capacity
def knapSack(c, w, v):


    if w is None or v is None or len(w) != len(v) or c< 0:
        return -1

    #init the array
    '''
    // Initialize a table where individual rows represent items
    // and columns represent the weight of the knapsack
    '''
    n = len(w)

    # columns first and rows later
    dp = [[0] * (c+1)] * (n+1 )

    for i in range(1, n +1):

        # get the value and weight of the item in the row above it
        weight = w[i-1]
        value = v[i-1]

        # remember the column represents the possible size
        for size in range(1, c+1):
            '''
            Consider not picking this item, remember if 
            the values in the 2 rows (are the same) -> we did not pick the item
            '''
            dp[i][size] = dp[i-1][size]

            '''
            Consider the cur elem and see if including this 
            would be more profitable and there is still room left 
            '''
            if size>= weight and dp[i-1][size - weight] + value> dp[i][size]:
                dp[i][size] = dp[i-1][size- weight] + value

    capacity = c
    itemSelected = []

    '''
    This is from same from our notes as well 
     Using the information inside the table we can backtrack and determine
 which items were selected during the dynamic programming phase. The idea
 is that if DP[i][sz] != DP[i-1][sz] then the item was selected
    '''
    for i in range(n,1,  -1):
        print('value of i is', dp[i][capacity])
        if dp[i][capacity] != dp[i-1][capacity]:
            itemIndex = i-1
            # print('the value selected is', itemIndex)
            itemSelected.append(itemIndex)

            #we have to minus the value here
            capacity -= w[itemIndex]

    # then return the items that were selected as said

    return dp[len(w)][c]


c = 10
v = [1, 4, 8, 5]
w = [3, 3, 5, 6]
print(knapSack(c, v, w))