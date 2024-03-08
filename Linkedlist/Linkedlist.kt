package LinkedList

class SinglyLinkedList {
    private var head: ListNode? = null

    class ListNode( // Can be a generic type
            val data: Int) {
        var next // Reference to next ListNode in list
                : ListNode? = null
    }

    fun display() {
        var current = head
        while (current != null) {
            print(current.data.toString() + " --> ")
            current = current.next
        }
        print("null")
        println()
    }

    fun length(): Int {
        if (head == null) {
            return 0
        }
        var count = 0
        var current = head
        while (current != null) {
            count++
            current = current.next
        }
        return count
    }

    fun insertFirst(value: Int) {
        val newNode = ListNode(value)
        // Update the header here
        newNode.next = head
        head = newNode
    }

    fun insert(position: Int, value: Int) {
        // 1 -> 4 -> 5
        // 1 -> 6 -> 4 -> 5
        val node = ListNode(value)
        if (position == 1) {
            node.next = head
            head = node
        } else {
            var previous = head
            var count = 1 // position - 1
            while (count < position - 1) {
                previous = previous!!.next
                count++
            }
            val current = previous!!.next
            previous.next = node
            node.next = current
        }
    }

    fun insertLast(value: Int) {
        val newNode = ListNode(value)
        if (head == null) {
            head = newNode
            return
        }
        var current = head
        while (null != current!!.next) {
            current = current.next
        }
        current.next = newNode
    }

    fun deleteFirst(): ListNode? {
        if (head == null) {
            return null
        }
        val temp= head
        head = head!!.next
        temp!!.next = null
        return temp
    }

    // Delete a node at given position
    fun delete(position: Int) {
        // position is valid and starting from 1
        // 3 -> 4 -> 7 -> 8 -> 9 -> null

        // If head is deleted then this becomes
        // 4-> 7 - 8 - 9  - null
        if (position == 1) {
            head = head!!.next

            // 4-> 7 - 8 - 9  - null
            // if delete 8
            // 7 should now point to 9
        } else {
            var previous = head
            var count = 1

            // Traverse to this node first
            while (count < position - 1) {
                previous = previous!!.next
                count++
            }

            // 7 - 8 - 9
            // 8 will be the current here
            val current = previous!!.next
            // point 7 to 9 for now instead of 8
            previous.next = current!!.next
        }
    }

    fun deleteLast(): ListNode? {
        if (head == null) {
            return head
        }
        if (head!!.next == null) {
            val temp = head
            head = head!!.next
            return temp
        }
        var current = head
        var previous: ListNode? = null
        while (current!!.next != null) {
            previous = current
            current = current.next
        }
        previous!!.next = null // break the chain
        return current
    }

    fun find(searchKey: Int): Boolean {
        if (head == null) {
            return false
        }
        var current = head
        while (current != null) {
            if (current.data == searchKey) {
                return true
            }
            current = current.next
        }
        return false
    }

    fun reverse(): ListNode? {
        if (head == null) {
            return null
        }
        var current = head
        var previous: ListNode? = null
        var next: ListNode? = null
        while (current != null) {
            next = current.next
            current.next = previous
            previous = current
            current = next
        }
        return previous
    }

    val middleNode: ListNode?
        get() {
            if (head == null) {
                return null
            }
            var slowPtr = head
            var fastPtr = head
            while (fastPtr != null && fastPtr.next != null) {
                slowPtr = slowPtr!!.next
                fastPtr = fastPtr.next!!.next
            }
            return slowPtr
        }

    fun getNthNodeFromEnd(n: Int): ListNode? {
        if (head == null) {
            return null
        }
        require(n > 0) { "Invalid value: n = $n" }
        var mainPtr = head
        var refPtr = head
        var count = 0
        while (count < n) {
            requireNotNull(refPtr) { "$n is greater than the number of nodes in list" }
            refPtr = refPtr.next
            count++
        }
        while (refPtr != null) {
            refPtr = refPtr.next
            mainPtr = mainPtr!!.next
        }
        return mainPtr
    }

    fun insertInSortedList(value: Int): ListNode {
        val newNode = ListNode(value)
        if (head == null) {
            return newNode
        }
        var current = head
        var temp: ListNode? = null
        while (current != null && current.data < newNode.data) {
            temp = current
            current = current.next
        }
        newNode.next = current
        temp!!.next = newNode
        return head!!
    }

    fun deleteNode(key: Int) {
        var current = head
        var temp: ListNode? = null
        if (current != null && current.data == key) {
            head = current.next
            return
        }
        while (current != null && current.data != key) {
            temp = current
            current = current.next
        }
        if (current == null) {
            return
        }
        temp!!.next = current.next
    }

    fun containsLoop(): Boolean {
        var fastPtr = head
        var slowPtr = head
        while (fastPtr != null && fastPtr.next != null) {
            fastPtr = fastPtr.next!!.next
            slowPtr = slowPtr!!.next
            if (fastPtr === slowPtr) {
                return true
            }
        }
        return false
    }

    fun startNodeInALoop(): ListNode? {
        var fastPtr = head
        var slowPtr = head
        while (fastPtr != null && fastPtr.next != null) {
            fastPtr = fastPtr.next!!.next
            slowPtr = slowPtr!!.next
            if (fastPtr === slowPtr) {
                return getStartingNode(slowPtr)
            }
        }
        return null
    }

    private fun getStartingNode(slowPtr: ListNode?): ListNode? {
        var slowPtr = slowPtr
        var temp = head
        while (temp !== slowPtr) {
            temp = temp!!.next
            slowPtr = slowPtr!!.next
        }
        return temp // starting node of the loop
    }

    fun removeLoop() {
        var fastPtr = head
        var slowPtr = head
        while (fastPtr != null && fastPtr.next != null) {
            fastPtr = fastPtr.next!!.next
            slowPtr = slowPtr!!.next
            if (fastPtr === slowPtr) {
                removeLoop(slowPtr)
                return
            }
        }
    }

    private fun removeLoop(slowPtr: ListNode?) {
        var slowPtr = slowPtr
        var temp = head
        while (temp!!.next !== slowPtr!!.next) {
            temp = temp!!.next
            slowPtr = slowPtr!!.next
        }
        slowPtr!!.next = null
    }

    fun createALoopInLinkedList() {
        val first = ListNode(1)
        val second = ListNode(2)
        val third = ListNode(3)
        val fourth = ListNode(4)
        val fifth = ListNode(5)
        val sixth = ListNode(6)
        head = first
        first.next = second
        second.next = third
        third.next = fourth
        fourth.next = fifth
        fifth.next = sixth
        sixth.next = third
    }

    companion object {
        fun merge(a: ListNode?, b: ListNode?): ListNode? {
            // a --> 1 --> 3 --> 5 --> null
            // b --> 2 --> 4 --> 6 --> null
            // result --> 1 --> 2 --> 3 --> 4 --> 5 --> 6 --> null
            var a = a
            var b = b
            val dummy = ListNode(0)
            var tail: ListNode? = dummy
            while (a != null && b != null) {
                if (a.data <= b.data) {
                    tail!!.next = a
                    a = a.next
                } else {
                    tail!!.next = b
                    b = b.next
                }
                tail = tail.next
            }

            // a --> 1 --> 3 --> null
            // b --> 2 --> 4 --> 6 --> 7 --> 9 --> 10 --> null
            // result --> 1 --> 2 --> 3 --> 4 --> 6 --> 7 --> 9 --> 10 --> null
            if (a == null) {
                tail!!.next = b
            } else {
                tail!!.next = a
            }
            return dummy.next
        }

        @JvmStatic
        fun main(args: Array<String>) {
            val sll1 = SinglyLinkedList()
            sll1.insertLast(1)
            sll1.insertLast(4)
            sll1.insertLast(8)
            val sll2 = SinglyLinkedList()
            sll2.insertLast(3)
            sll2.insertLast(5)
            sll2.insertLast(8)
            sll2.insertLast(9)
            sll2.insertLast(14)
            sll2.insertLast(18)
            sll1.display()
            sll2.display()
            val result = SinglyLinkedList()
            result.head = merge(sll1.head, sll2.head)
            result.display()
        }
    }
}