package Dynamic_programming




// o: 2^n   2 calls for every function here
// SC: 2^n

// Store # calculated

fun fibRecur(n:Int):Int{
    if(n <=1){
        return n
    }
    return fibRecur(n-1) + fibRecur(n-2)

}


fun main(args: Array<String>) {
    val n = 9
    println(fibRecur(n))
}