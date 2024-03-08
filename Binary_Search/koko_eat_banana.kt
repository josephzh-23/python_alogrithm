package Binary_search

/*
h : the bananas per hour se
 */
fun minEatingSpeed(piles:IntArray, h: Int): Int {

    var (left, right) = Pair(0, piles.max()!!)

    while(left< right){

        var mid = left + (right - left) /2
        if(canEatIntTime(piles, mid, h)){
            right = mid - 1
        }else{
            right = mid + 1
        }
    }
    return left
}

/*
The time complexity here isbacailly
O(n * log(m))

n: the number of piles and m: the range here
 This basically lets you know if a pile can be finished within the eating speed

 if you have pile = 10
 h = 4
 need 2 hours + 10%
 */

fun canEatIntTime(piles: IntArray, k: Int, h: Int): Boolean {
    var hours = 0
    for (pile in piles) {
        var div = pile / k
        hours += div
        if (pile % k != 0) hours++
    }
    return hours <= h
}
