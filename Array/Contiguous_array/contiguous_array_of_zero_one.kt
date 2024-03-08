package Array.Contiguous_array

import java.lang.Math.max


// Put the count into the hashmap here
/*
The map here wouldb e sth like the followign
-1  0  1  0
[0, 1, 1, 0, 1, 1, 0, 1]
 */
fun maxLength(nums: IntArray): Int {
    // Save the count at each index as noted

    var indexToCount = mutableMapOf<Int, Int>()
    indexToCount[0] = -1
    var maxLength  =0
    var count = 0
    for(i in 0 until nums.size){
        // To offset th eocunt here
        if(nums[i]== 0){
            count+=-1
        }else{
            count+=1
        }

        if(indexToCount.contains(count)){
            // current index - the previous index here
            maxLength = max(maxLength, i- indexToCount.get(count)!!)
        }else{
            indexToCount.put(count ,i)
        }
        indexToCount[count] = i
    }
    return maxLength
}