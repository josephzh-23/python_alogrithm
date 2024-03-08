//package Tree
//
//import java.util.*
//
//// This is a better solution then even before
//
//fun populateNextPointer(r: SpecialNode?): SpecialNode? {
//
//    if(r==null) return null
//    var q : Queue<SpecialNode> = LinkedList()
//    q.add(r)
//    while (!q.isEmpty()) {
////        val curLevel = ArrayList<Int>()
//        // The num of nodes in cur level
//
//        // The dummy will be here @ the beginning of each level
//        var dummy = SpecialNode(0, null, null, null)
//        for (i in 0 until q.size) {
//            val node = q.remove()
//
//            dummy.next = node
//            dummy = dummy.next!!
//            node.left?.let {
//                q.add(it)
//
//            }
//            node.right?.let {
//                q.add(it)
//                node.left?.next = node.right
//            }
//        }
//
//    }
//    return r
//}