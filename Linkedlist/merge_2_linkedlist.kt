package LinkedList

fun mergeTwoLists(l1: ListNode?, l2: ListNode?): ListNode? {
    // Use a temp node first with a 0 hold the head's
    // return temp
    var l1 = l1
    var l2 = l2
    // This temp node allows us to return the head of
    // the merged list later
    val tempNode = ListNode(0)
    var curNode: ListNode? = tempNode
    while (l1 != null && l2 != null) {
        if (l1.value < l2.value) {
            curNode!!.next = l1
            l1 = l1.next
        } else {
            curNode!!.next = l2
            l2 = l2.next
        }
        curNode = curNode.next
    }
    curNode
    if (l1 != null) {
        curNode!!.next = l1
        l1 = l1.next
    }
    if (l2 != null) {
        curNode!!.next = l2
        l2 = l2.next
    }
    printLinkedList(tempNode)
    return tempNode.next
}

fun main() {

    var list1 = ListNode(1)
    append(list1, 2)
    append(list1, 3)
    append(list1, 4)

    var list2 = ListNode(6)
    append(list2, 7)
    append(list2, 8)
    append(list2, 9)

    mergeTwoLists(list1, list2)


}