package Sliding_window


fun main() {
    var prices = intArrayOf(7, 1, 5, 3, 6, 4)
    print(maxProfit(prices))
}

fun maxProfit(prices: IntArray): Int {
    var profit = 0
    for (i in 1 until prices.size) {
        if (prices[i] > prices[i - 1]) {
            profit += (prices[i] - prices[i - 1])
        }

    }
    return profit
}