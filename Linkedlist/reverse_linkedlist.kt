package LinkedList


// O(n)
internal class Solution {
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
}