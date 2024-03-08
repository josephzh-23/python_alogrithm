package Array

/*
This gives you the next permutation here
And then becomes as we said here
 */

/*
Find the point of change here
The # starts changing from 1st decreasing sequence from the end

1 1 5 4 6
1 1 5 6 4

Step 2: Find the next highest number present after the current number
and rearrange these numbers

step 3: rearrange the rest of the numbers to make sure it fits here

[1, 2, 3]
[1, 3, 2]
 */
fun nextPermutation(nums: IntArray) {
    var i = nums.size - 2

    // From teh back of the array
    // Find the point where at i nums[i] < nums[i + 1]
    while (i >= 0 && nums[i + 1] <= nums[i]) {
        i--
    }

    /*
     If i >= 0 then find the next biggest element bigger then
        current element
     */
    if (i >= 0) {
        var j = nums.size - 1
        while (nums[j] <= nums[i]) {
            j--
        }
        swap(nums, i, j)
    }
    reverse(nums, i + 1)
    nums.forEach{
        println(it)
    }
}

private fun reverse(nums: IntArray, start: Int) {
    var i = start
    var j = nums.size - 1
    while (i < j) {
        swap(nums, i, j)
        i++
        j--
    }
}

private fun swap(nums: IntArray, i: Int, j: Int) {
    val temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
}

fun main() {
    var arr = intArrayOf(1, 2, 3)

    print(nextPermutation(arr))
}






