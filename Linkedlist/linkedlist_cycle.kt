package LinkedList

// Using a slow and a fast pter,
//. The slow pointer moves one step at a
// time while the fast pointer moves two steps at a time.

class Solution14 {
    fun hasCycle(head: ListNode?): Boolean {
        if (head == null) {
            return false
        }
        var slow = head
        var fast = head.next
        while (slow != fast) {
            if (fast == null || fast.next == null) {
                return false
            }
            slow = slow!!.next
            fast = fast.next!!.next
        }
        return true
    }
}