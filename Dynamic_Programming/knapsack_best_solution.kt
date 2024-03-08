package Dynamic_programming


/* O(n *c)

This is from William Fiest
storing results in 2d array n *c

So when do we include an element in knapsack?

 */


// With the knapsack problem here you will see that
object Knapsack_01 {
    /**
     * @param capacity - The maximum capacity of the knapsack
     * @param W - The weights of the items
     * @param V - The values of the items
     * @return The maximum achievable profit of selecting a subset of the elements such that the
     * capacity of the knapsack is not exceeded
     */
    fun knapsack(capacity: Int, W: IntArray?, V: IntArray?): Int {
        require(!(W == null || V == null || W.size != V.size || capacity < 0)) { "Invalid input" }
        val N = W.size


        // Knapsack table

        // Initialize a table where individual rows represent items
        // So whether to include an item
        // and columns represent the weight of the knapsack
        // All have ot be +1 as indicated
        val DP = Array(N + 1) { IntArray(capacity + 1) }


        // It's better to make this 1-based
        for (i in 1..N) {

            // Get the value and weight of the item
            val w = W[i - 1]
            val v = V[i - 1]
            for (curCap in 1..capacity) {
                println("value is $v")
                // 2 cases: pick or not pick the element
                // Consider not picking this element
                // This would be directly 1 row above
                DP[i][curCap] = DP[i - 1][curCap]

                // Check if we can get a better value if we were to include current item
                // Consider including the current element and
                // see if this would be more profitable
                if (curCap >= w && DP[i - 1][curCap - w] + v > DP[i][curCap])
                    DP[i][curCap] = DP[i - 1][curCap - w] + v
            }
        }


        // Part 2: this part is completely optional for printing out the stuff
        var sz = capacity
        val itemsSelected: MutableList<Int> = ArrayList()

        // Using the information inside the table we can backtrack and determine
        // which items were selected during the dynamic programming phase. The idea
        // is that if DP[i][sz] != DP[i-1][sz] then the item was selected
        for (i in N downTo 1) {
            if (DP[i][sz] != DP[i - 1][sz]) {
                val itemIndex = i - 1
                itemsSelected.add(itemIndex)
                sz -= W[itemIndex]
            }
        }

        // Return the items that were selected
        // java.util.Collections.reverse(itemsSelected);
        // return itemsSelected;

        // this Return the maximum profit
        return DP[N][capacity]
    }

    @JvmStatic
    fun main(args: Array<String>) {
        var capacity = 10
        var V = intArrayOf(1, 4, 8, 5)
        var W = intArrayOf(3, 3, 5, 6)
        println(knapsack(capacity, W, V))
//        capacity = 7
//        V = intArrayOf(2, 2, 4, 5, 3)
//        W = intArrayOf(3, 1, 3, 4, 2)
//        println(knapsack(capacity, W, V))
    }
}

