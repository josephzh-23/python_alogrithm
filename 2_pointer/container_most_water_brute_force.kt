package Array.two_pointer

fun containMostWaterBF(height:IntArray):Int{

    var max = Integer.MIN_VALUE
    for(i in 0 until height.size){
        for(j in i+1 until height.size){
            var min = Math.min(height[i], height[j])
            max = Math.min(max, min*(j-i))
        }
    }
    return max
}