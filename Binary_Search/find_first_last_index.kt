package Binary_search

/*
Basically we have to take care of the case where
5, 7, 7, 8, 8, 8
        L   M  R
   where you have the above we return the one on the right
 */


'''
Say in the example that we have the following here
2. Determine the first and last position of elem:


2, 7, 7, 7, 8, 10       target is 8


And using the above number 7 the first index in the element here,

In the lower bound case:

mid = (0 + 5) / 2 = 2 here
nums[2 - 1] = nums[1] (7) = 7
7 < 8

end = mid (2) - 1 = 1
so the lower bound is 7


In the upper bound case:

To find the upper bound here:




'''
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
fun main() {

    // Have to be careful of the 3 8 cases here
    val arr = intArrayOf(5, 7, 7, 8, 8,8, 10)
   var res = searchRange(arr, 8)
    print(res[0])
    print(res[1])
}
fun searchRange(nums: IntArray, target: Int): IntArray {
    val left = binarySearch(nums, target, true)
    val right = binarySearch(nums, target, false)
    return intArrayOf(left, right)
}

private fun binarySearch(nums: IntArray, target: Int, leftBias: Boolean): Int {
    var index = -1
    var start = 0
    var end = nums.size - 1

    // Standard binary search
    while (start <= end) {
        val mid = start + (end - start) / 2

        '''

        '''
        if (target > nums[mid]) {
            start = mid +1  // Look in the right sub-array
        } else if (nums[mid] > target){
            end = mid -1     // look in the left sub-array
        }else {
            index = mid
            if(leftBias){
                end = mid - 1
            }else{
                start = mid  + 1
            }
        }
    }
    return index
}
