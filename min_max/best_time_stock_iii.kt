package min_max

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
fun maxProfit3(prices: IntArray): Int {

    var buy1 = prices[0]
    var buy2 = prices[1]
    var firstBuy = Integer.MIN_VALUE
    var secondBuy = Integer.MAX_VALUE
    var firstSell = 0; var secondSell = 0
    for(i in prices.indices){

        firstBuy = Math.max(firstBuy, -prices[i])
        firstSell = Math.max(firstBuy, firstBuy + prices[i])
        secondBuy = Math.max(secondBuy, firstSell-prices[i])
        secondSell = Math.max(firstBuy, secondBuy+ prices[i])
    }
    return secondSell
}











