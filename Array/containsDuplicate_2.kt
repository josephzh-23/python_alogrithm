package Array


fun containsDuplicate(nums:IntArray, k: Int):Boolean{
   // https://leetcode.com/problems/contains-duplicate-ii/
    var map: MutableMap<Int, Int> = HashMap()
    for(i in nums.indices){
        val cur = nums[i]
        if(map.containsKey(cur) &&i- map.get(cur)!! <=k){
            return true
        }else{
            // 3, 1      3 is the start as mentioned
            // 1 is the position
            map.put(cur, i)
        }
    }
    return false
}