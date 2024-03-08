package Hard

import java.util.*


fun getNumberOfBacklogOrders(orders: Array<IntArray>): Int {
    val buy = PriorityQueue { a: IntArray, b: IntArray ->
        b[0] - a[0]
    }
    val sell = PriorityQueue { a: IntArray, b: IntArray ->
        a[0] - b[0]
    }
    for (o in orders) {
        if (o[2] == 0) { // processing buy orders:

            // If the price of buy > price of sell
            // And also the amount is bigger
            while (!sell.isEmpty() && o[0] >= sell.peek()[0] && o[1] >= sell.peek()[1]) {
                o[1] -= sell.peek()[1]

                // Drop the price here
                sell.poll()
            }

            // If the price of buy > price of sell
            // And also the amount is bigger
//            if (!sell.isEmpty() && o[0] >= sell.peek()[0] && o[1] > 0) {
//                sell.peek()[1] -= o[1]
//                o[1] = 0
//            }

            // When buy amount > 0 then add here
            if (o[1] > 0) {
                buy.offer(o)
            }
        } else { // processing sell orders:
            while (!buy.isEmpty() && o[0] <= buy.peek()[0] && o[1] >= buy.peek()[1]) {
                o[1] -= buy.peek()[1]
                buy.poll()
            }
//            if (!buy.isEmpty() && o[0] <= buy.peek()[0] && o[1] > 0) {
//                buy.peek()[1] -= o[1]
//                o[1] = 0
//            }
            if (o[1] > 0) {
                sell.offer(o)
            }
        }
    }
    var res: Long = 0
    for (o in sell) {
        res += o[1].toLong()
    }
    for (o in buy) {
        res += o[1].toLong()
    }
    return (res % 1000000007).toInt()
}