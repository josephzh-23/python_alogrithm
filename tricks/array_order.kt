package tricks

// Given an alphabetical order and then
/*
"hlabcdefgijkmnopqrstuvwxyz"    notice in this order h comes before l here

Use an order array and then we can store each variable in it based on position
 */
fun orderLetterArray(order:String){

    val orderMap = IntArray(26)
    for(i in 0 until order.length){
        var char = order[i]
        orderMap[char.code - 'a'.code] = i
    }
}