import LinkedList.ListNode
import LinkedList.append
import LinkedList.printLinkedList
import Util.printList


// Delete an item in linekdlist
// O(1)

fun main() {
    var i = ListNode(1)

    append(i, 4)
    append(i, 5)
    append(i, 6)
//    printLinkedList(i)

    deleteAtPosition(i, 1)
    printLinkedList(i)

}

fun deleteAtPosition(head: ListNode?, pos: Int) {

    // store the header here
    var cur = head
    var count = 0

    // case 1 the head needs to be removed here
    if (pos == 0) {
        cur = cur?.next
    }

    // Find the previous node of hte node to be deleted
    while (count < pos - 1 && cur != null) {

        cur = cur.next
        count++
    }

    // If position is more than the # of nodes here
    if (cur?.next == null) return


    // You have found the node at the deletion point
    // and then do the deletion
    val next = cur.next?.next

    cur.next = next

}

