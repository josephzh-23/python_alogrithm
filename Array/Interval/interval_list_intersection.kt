package Array.Interval


// https://leetcode.com/problems/interval-list-intersections/description/

/*
You are basically combining the 2 lists here
 */
fun main() {
    // val start list and the end list here
    var firstList = arrayOf(
        intArrayOf(0,2 ), intArrayOf(5, 10),
        intArrayOf(13, 23), intArrayOf(24, 25)
    )

    var secondList = arrayOf(
        intArrayOf(1, 5), intArrayOf(8, 12), intArrayOf(15, 24),
        intArrayOf(25, 26)
    )
    var outputArray = Array(firstList.size){IntArray(2)}
    // Use a 2 pter solution
    var l = 0
    // For the 2nd one here
    // [1, 5] , [0, 2] since 5 [1, 2]
    // l++ this stops when one reaches the end correct?
    var r = 0
    var k = 0
    while(l < firstList.size && r < secondList.size){

        // 2nd iter: r = 0, l : 1
        /*
        3rd case
        [5, 10]
        [1, 5]
          r++       [5, 5]
         */
        var firstElem = firstList[l]
        var secondElem = secondList[r]

        // take care of 2nd elem at each index
        if(firstElem[1] < secondElem[1]){
            outputArray[k][1] = firstElem[1]
        }else{
            outputArray[k][1] = secondElem[1]
        }
        /*
         [0, 2]
         [1, 5]
         [1, 2]
         */
        // take care of first elem at each index
        if(firstElem[0] < secondElem[0]){
            outputArray[k][1] = firstElem[1]
            r++
        }else{
            outputArray[k][1] = secondElem[1]
            l++
        }
    }

}

