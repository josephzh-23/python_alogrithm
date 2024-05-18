package min_max


// The problem seems very simple but upon a closer look maybe not
// so much as said

fun main() {
    var nums = intArrayOf(0, 1)

    // As we loop through the array here
    // Check the current number


    // The count varialbe here
    // which is used to store the relative number of
// ones and zeros encountered so far while traversing the array.
// The countcountcount variable is incremented by one for every 1 encountered and the same is decremented by one for every
// 0 encountered.

    // Put the count into a hashmap here

}

fun findMaxLength(nums: IntArray){

    var counts = mutableMapOf<Int, Int>()
    var maxLength = 0
    var count = 0
    for(i in 0 until nums.size){
        if(nums[i] ==0){
            count+=-1
        }else{
            count+=1
        }

        if(counts.containsKey(count)){
            maxLength = Math.max(maxLength, i- counts.get(count)!!)
        }else{
            counts[count] = i
        }
    }
}
