package Dynamic_programming


/*

At each point in the code, we can decide whether to put an item
in the bag
        A   B   C   D
profit  1   6   10  16          capacity 7
weight  1   6   3   5

In each decision, we have a decision to put or not put
At the end
O ( 2 ^n)
This is the slow approach as dicsussed
So we start from the back of the array as discussed
def ks(n, c):

    v[n]       the value array
// nothing left to return because no more capacity
    if n ==0 or c ==0: // base case
        result = 0

    if cur wt > c , then move to left
    else if w[n] > c:
        result = ks(n-l, c)

        case3: try uptting item in knapsack and not putting
        it there with tmp1 and tmp2 and check the maximum result
        tmp1 -> !put in ksack
        tmp2 -> put in sack, we will add v[n] curr item value
    else:
        tmpI = ks(n-1, c)
        tmp2 = v[n] + ks(n-1, c- w[n])
        result = max(tmp1, tmp2)

 */
class KnapsackBruteForce(private val profits: IntArray, private val weights: IntArray) {
    // brute force
    fun solveKnapsack(capacity: Int): Int {
        return helper(0, capacity, 0)
    }

    // Index for each and every single item
    private fun helper(index: Int, capacity: Int, curProfits: Int): Int {

        // Make sure this > 0 for capacity case
        if (capacity < 0) return 0

        // If our current index > prfits array, then return the profits
        if (index >= profits.size) {
            return curProfits
        }

        // You get the maximum of the profit her e

        // take current item, capacity decreasing, current item increasing
        val take = helper(index + 1, capacity - weights[index], curProfits + profits[index])

        // skip current item
        val skip = helper(index + 1, capacity, curProfits)
        return Math.max(take, skip)
    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            /**
             * Input: values = [1, 6, 10, 16] weights = [1, 2, 3, 5] maxWeight = 7
             *
             * Max is 22
             */
            val test0 = KnapsackBruteForce(intArrayOf(1, 6, 10, 16), intArrayOf(1, 2, 3, 5))
            println(test0.solveKnapsack(7)) // <--- expect 22
            /**
             * Input: values = [60, 50, 70, 30] weights = [5, 3, 4, 2] maxWeight = 8
             *
             * Output: 120
             */
            val test1 = KnapsackBruteForce(intArrayOf(60, 50, 70, 30), intArrayOf(5, 3, 4, 2))
            println(test1.solveKnapsack(8)) // <--- expect 120
            /**
             * Input: values = [60, 100, 120, 80, 30] weights = [10, 20, 30, 40, 50]
             * maxWeight = 400
             *
             * Output: 390
             */
            val test2 = KnapsackBruteForce(intArrayOf(60, 100, 120, 80, 30), intArrayOf(10, 20, 30, 40, 50))
            println(test2.solveKnapsack(400)) // <--- expect 390
        }
    }
}