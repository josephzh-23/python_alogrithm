package LinkedList

fun main() {
    var i = ListNode(1)

    append(i, 4)
    append(i, 5)
    append(i, 5)
    append(i, 6)
//    printLinkedList(i)

    deleteSorted(i, 1)
    printLinkedList(i)

}

fun deleteSorted(head: ListNode?, pos: Int) {

    // store the header here
    var cur = head
    var count = 0

    var prev :ListNode?= null
    // case 1 the head needs to be removed here
    if (pos == 0) {
        cur = cur?.next
    }


    // Find the previous node of hte node to be deleted
    while (cur != null) {

        // This will then do the deletino here
        if(cur.value == cur.next?.value){
            prev?.next = cur.next
        }else{
            prev = cur
        }
        cur = cur.next
        count++
    }

}
