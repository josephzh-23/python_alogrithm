package Array.two_pointer

/*

while heights[i] <= heights[j]

maxLeft = max(height[i] , maxLeft)
water  = water + maxLeft - height[i]

while heights[j] > heights[i]
water = water + maxLeft - height[j]
 */

fun trap(height: IntArray): Int {
    var (i, j, maxLeft, maxRight, water) =
        listOf(0, height.size -1, 0, 0, 0)

    while(i < j){
        if(height[i]<=height[j]){
            // maxLeft
            maxLeft = Math.max(maxLeft, height[i])
            water+= maxLeft- height[i]
            i++
        }else{
            //maxRight
            maxRight = Math.max(maxRight, height[j])
            water+= maxRight - height[j]
            j--
        }
    }
    return water
}