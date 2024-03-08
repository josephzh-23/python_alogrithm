package tricks

fun main() {
    maxSwap(12333)
}
fun maxSwap(num: Int){
    // Need to store up to 10 digits as said
    var occur = IntArray(10)
    var numArr= num.toString().toCharArray()
// Store last index of each letter
    for (i in 0 until numArr.size) {
        occur[numArr[i]- '0'] +=1
    }
   occur.forEach{
       println(it)
   }
}