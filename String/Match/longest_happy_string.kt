package String.Hard

import January_3rd.print
import java.util.*

fun main() {
    var (a, b, c ) = intArrayOf(1, 1, 7)
    longestDiverseString(a, b, c).print()
}


class Custom(var value: Char, var count: Int)

// And then you have the 'a', 'b', 'c' here and then
fun longestDiverseString(a: Int, b: Int, c: Int): String { // The character and then the count
    var map = mutableMapOf<Char, Int>()

    val pq = PriorityQueue<Custom> { a, b -> b.count - a.count }

    if (a > 0) {
        pq.add(Custom('a', a))
    }
    if (b > 0) {
        pq.add(Custom('b', b))
    }
    if (c > 0) {
        pq.add(Custom('c', c))
    }

    var sb = StringBuilder() // 0th index -> letter
    // 1 index -> count
    var curInfo = intArrayOf(0, 0)
    while (!pq.isEmpty()) {


        var c1 = pq.poll()
        var value = c1.value - 'a' // The first one of its kind
        if (curInfo[0] != value) {
            curInfo[0] = value
            curInfo[1] = 1
            sb.append(c1.value)

            // A duplicate of what happened before
            // we are seeing 2 more here
        } else if (curInfo[1] + 1 < 3){
            curInfo[1]++
            sb.append(c1.value)
            c1.count--

            /*
           The case where you already have
           "aa"   and it's about to surpass and then you have to do sth else
             */
        }else if (!pq.isEmpty()){

            // COuld be b
            var c2 = pq.poll()
            curInfo[0] = c2.value - 'a'
            curInfo[1] = 1
            sb.append(c2.value)
            c2.count--
            if(c2.count> 0){
                pq.add(c2)
            }
        }else{
            break
        }
        if(c1.count > 0){
            pq.add(c1)
        }
    }
    return sb.toString()
}