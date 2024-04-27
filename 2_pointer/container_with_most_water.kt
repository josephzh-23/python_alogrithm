package Array.two_pointer//package tricks.two_pointer
///*
//The formula
//area = (R- L) * min(height[l], height[r])
//1. If height[r] < height[l]
//    r--
//2. If height[r] > height[l]
//    l++
//3. If height[r] = height[l]
//    r-- , l++       move both pointers
// */
//fun containMostWater(height:IntArray):Int{
//
//    var n = height.size
//    // We want the results to see
//    // We need to grab the minimum at each height
//    // If grab maximum water would overflow here
//    var left = 0
//    var right = n-1
//    var max = 0
//    while(left< right){
//        var lh = height[left]
//        var rh = height[right]
//        var w = right- left
//        var h = Math.min(lh, rh)
//        var area = w* h
//        max = Math.max(max, area)
//        if(lh< rh){
//            left++
//        }else if(rh< lh){
//            right--
//        }else{
//            left++
//            right--
//        }
//    }
//    return max
//}