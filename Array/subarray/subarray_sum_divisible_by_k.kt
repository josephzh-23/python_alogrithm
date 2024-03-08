package Array.subarray


/*
[4, 5, 0, -2, -3, 1]    5

4 % 5 = 4
dict[4] = 1     now     using the prefix sum then
add 4 + 5 = 9

and 9 % 5 = 4 -> dict[4] =2 now use the same approach here
The reason the above works is because

9 - 4 = 5 which is % 5 = 0 here
 */

fun main() {
    var nums = intArrayOf(4, 5, 0, -2, -3, 1)
    subArraySumByK(nums , 5)
}
fun subArraySumByK(nums: IntArray, k: Int){

    var (prefixSum, count) =IntArray(2){0}
    var dict= mutableMapOf<Int, Int>()

    dict[0] = 1
    for(num in nums){
        prefixSum += num
        if(dict.contains(prefixSum % k)){
            count += dict[prefixSum %k]!!
        }

        dict.putIfAbsent(prefixSum%k, 0)
        dict[prefixSum % k] = dict[prefixSum % k]!! + 1
    }

    println("the answ is $count")
}