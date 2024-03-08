package Tree.Array

/*
Use slow, fast prev to head

Slow will move 1 step @ a time
The fast pter move 2 steps at a time
 */


import LinkedList.ListNode
import Tree.Basic.TreeNode

internal class Solution12 {
    lateinit var nums: IntArray
    fun sortListToBST(head: ListNode): TreeNode? {
        val mid = findMidPoint(head)
        val root = TreeNode(mid?.value!!)

        if (head == mid)
            return root

        root.left = sortListToBST(head)
        root.right = sortListToBST(mid.next!!)
        return root
    }

    /*
    The idea is to find the mid and break previous links
    Have slow, fast and prev here
    Assign prev to slow, move slow 1 step and move fast 2 steps here
     */

    /*
    Basically when fast reaches the end then the mid will be at the
    middle here
     */
    fun findMidPoint(head: ListNode?): ListNode? {
        var fast = head
        var slow = head
        var prev = head

        while (fast != null && fast.next != null) {
            prev = slow
            slow = slow?.next
            fast = fast?.next?.next
        }
        // If prev is not null then break link between prev and prev.next
        if (prev != null) {
            prev.next = null
        }
        return slow
    }
}

