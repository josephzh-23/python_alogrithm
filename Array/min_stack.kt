package Array//package Stacks_Queue
//
//import java.lang.Integer.min
//import java.util.*
//
//fun Sliding_window.Basic.Sliding_window.Graph.Hard.main() {
//    var s = minStack()
//    s.push(-1);
//    s.push(10);
//    s.push(-4);
//    s.push(0);
//    println(s.getMin())
//    println(s.pop())
//    println(s.pop())
//    println(s.getMin())
//}
//class minStack(){
//
//    // at ith idx, it will contain the smallest elem up to
//    // that index in the array here
//    // [1, 2, 3,4,3]
//    // Use a stack with a pair [min, the value]
//    var s = Stack<Pair<Int,Int>>()
//
//    fun push(x: Int) {
//
//        // case 1 stack empty
//        if(s.isEmpty()){
//            // Both would be the min here
//            s.push(Pair(x,x))
//
//        }else {
//           // compare the min with the new val
//            var min = min(s.peek().second, x )
//            s.push(Pair(x, min))
//        }
//
//    }
//
//    // when removing here
//    fun pop(): Int{
//        return s.pop().first
//    }
//
//    // Here no need to pop just return top
//    fun top(): Int {
//        return s.peek().first
//    }
//
//    fun getMin(): Int {
//        return s.peek().second
//    }
//}