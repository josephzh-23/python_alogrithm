package palindrome

import LinkedList.ListNode


internal class Solution {
    fun isPalindrome(head: ListNode): Boolean {
        var head: ListNode = head

        /*
        The fast here is for finding the middle point
         */
        var fast: ListNode = head
        var slow: ListNode = head
        while (fast.next != null && fast.next!!.next != null) {
            slow = slow.next!!
            fast = fast.next!!.next!!
        }

        // 1, ||| 2.  ||||  3 --> slow = 2, fast = 3
        if (fast != null) slow = slow.next!!

        //Reverse the list start from slow.
        var revHead: ListNode? = reverse(slow)
        while (revHead != null) {
            if (revHead.value !== head.value) return false else {
                revHead = revHead.next
                head = head.next!!
            }
        }
        return true
    }

    fun reverse(head: ListNode?): ListNode? {
        var head: ListNode? = head
        var prev: ListNode? = null
        while (head != null) {
            val next: ListNode = head.next!!
            head.next = prev
            prev = head
            head = next
        }
        return prev
    }
}