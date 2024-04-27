package min_max

// the following is the max of 1s when you can flip only 1 element here

// max 1s here and then
fun main() {
    // and then over here we have the following

}

// k represents the number of 1s we can flip
fun maxOnesConsecs(arr: IntArray, k : Int){
    var maxConsecOnes = 0
    var (start, k , zeroCount) = listOf(0,0,0)

    /*
    So here we basically have
    s
    [1, 1, 0, 0, 1, 1, 1, 1, 1]
    e
    start will then move until we have more 0s count
    then originally asked for here
     */
    for(end in 0 until arr.size){
        if(arr[end] ==0){
            zeroCount++
        }

        while(zeroCount> k){
            if(arr[start] == 0){
                zeroCount--
            }
            start++
        }

        maxConsecOnes = Math.max(maxConsecOnes, end-start + 1)

    }
}