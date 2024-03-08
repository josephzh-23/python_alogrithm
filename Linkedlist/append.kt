 package LinkedList
// append to the end of the linkedlist as discussed as agreed
fun append(node: ListNode, value: Int) {

        var temp: ListNode = node

        // Get to the last one here
        while (temp.next != null) temp = temp.next!!
        temp.next = ListNode(value)

}