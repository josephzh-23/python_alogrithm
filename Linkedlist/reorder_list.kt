package LinkedList

/*
This problem is a combination of these three easy problems:
Middle of the Linked List.
Reverse Linked List.
Merge Two Sorted Lists.
 */


/*
A combinatino of middle of linkedlist
2. reverse linkedl ist
3. merge 2 sorted lists

Input    1  2  3  4  5  6  7  8
output   1 8 2  7  3  6  4  5

Take input list, split the list in middle
1 2 3 4
5 6 7 8     then reverse 2nd half
1 2 3 4
8 7 6 5     then just merge the 2 lists up here
 */
fun reorderList(head: ListNode): Unit {
//1.  Reverse the Second Part of the List and Merge Two Sorted Lists

    // If 2 middle use the second middle

    // head of first half
    var l1 = head

    // tail of the first list
    var prev: ListNode? = null
    //head of 2nd half
    var slow = head
    // tail of 2nd half of the list
    var fast = head


    while(fast!=null && fast.next!=null){
        prev = slow
        slow = slow.next!!
        fast = fast.next!!.next!!
    }

    // This splits the list into 2 here
    prev?.next = null

    var l2 = reverseList(slow)
    mergeTwoLists(l1, l2)
}


fun reverseList(head: ListNode?): ListNode? {
    // Null for the head
    var prev: ListNode? = null
    var curr: ListNode? = head
    while (curr != null) {

        // Use a temp to hold the next variable
        val nextTemp: ListNode? = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp
    }
    return prev
}

fun findMiddleNode(head: ListNode?): ListNode? {
    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {
        slow = slow!!.next
        fast = fast.next!!.next
    }
    return slow
}