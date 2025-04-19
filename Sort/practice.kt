//package sorting
//
//
//import Basics.printMatrix
//import java.util.*
//
//
//
//var meet3 = arrayOf(
//        intArrayOf(0, 30),
//        intArrayOf(5, 10), intArrayOf(15, 20)
//)
//
//
//fun Sliding_window.maining_window.Sliding_window.Graph.Hard.main() {
//    // Sort by the first element of each array
//    //
//    // the interval start -> end here
//    var count =0
//    Arrays.sort(meet3) { a, b -> a[0] - b[0] }
//    printMatrix(meet3)
//
//    for(i in 1 until meet3.size){
//        if(meet3[i-1][1] > meet3[i][1]){
//            count++
//        }
//    }
//    print(count)
//}