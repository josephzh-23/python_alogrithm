package Array

import java.lang.Integer.max

fun main() {
    var prices = intArrayOf(7, 1, 5, 3, 6, 4)
    buySellStock(prices)
}
fun buySellStock(prices: IntArray): Int {
    var maxi = 0
    // maximize the profit here
    // try sorting first
//    prices.sort()
    for(i in 1 until prices.size){
        for(j in i+1 until prices.size){
           var profit = prices[j] - prices[i]
            maxi = max(maxi, profit)
        }
    }
    return maxi.also{println(it)}
}