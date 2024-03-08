import LinkedList.ListNode

/*
    [[1, 4, 5], [1, 3, 4], [2, 6]]
    start       mid     mid +1      end     the 4 positions

    we use this to return the head of our list

    OC: O (n *log(k))       n the # of nodes we have when merging 2 lists
    k: # of recursive calls we have
    logk comes from the logk mergeKlists
 */
internal class Solution13 {
    fun mergeKLists(lists: Array<ListNode>?): ListNode? {
        return if (lists == null || lists.size == 0) null else mergeKLists(lists, 0, lists.size - 1)
    }

    // how does k come into play here?

    private fun mergeKLists(lists: Array<ListNode>, start: Int, end: Int): ListNode? {
        if (start == end) return lists[start]
        val mid = start + (end - start) / 2 // (start + end) /2;
        val left = mergeKLists(lists, start, mid)
        val right = mergeKLists(lists, mid + 1, end)
        return merge(left, right)
    }
    // This returns the head of our merged linkedlist
    private fun merge(l1: ListNode?, l2: ListNode?): ListNode? {

        // this is used
        var l1 = l1
        var l2 = l2

        // Curr is a dummy node first
        val result = ListNode(-1)
        var curr: ListNode? = result
        while (l1 != null || l2 != null) {
            if (l1 == null) {
                curr!!.next = l2
                l2 = l2!!.next
            } else if (l2 == null) {
                curr!!.next = l1
                l1 = l1.next
            } else if (l1.value < l2.value) {
                curr!!.next = l1
                l2 = l2.next
            }
            curr = curr!!.next
        }
        return result.next
    }
}