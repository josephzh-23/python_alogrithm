package LinkedList

fun findDuplicate(nums: IntArray): Int {

    var dup = 0
    // Without modifying the array nums
    //n + 1 integers
    // 1- 2 check same if same return if not
    // don't return
    // Only 1 repeated num in nums using O(1) space as said
    // Can not modify
    for (i in 0 until nums.size-1) {
        var node = ListNode(nums[i])

        if (node.value == nums[i + 1]) {
            dup = nums[i+1]
        } else {
            // Not found case
            node.next?.let {
                node = it
            }
        }
    }
    return dup.also{println(it)}
}

fun main(){

    var test = intArrayOf(1, 3, 4, 2,2)
    findDuplicate(test)
}