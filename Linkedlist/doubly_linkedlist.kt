package LinkedList

//https://www.geeksforgeeks.org/introduction-to-doubly-linked-lists-in-java/
class Node(var data: Int) {
    var prev: Node? = null
    var next: Node? = null
}

class DoublyLinkedList {
    var head: Node? = null
    var tail: Node? = null

    // Traversing from head to the end of the list
    fun traverseForward() {
        var current: Node? = head
        while (current != null) {
            print(current.data.toString() + " ")
            current = current.next
        }
    }

    // Traversing from tail to the head
    fun traverseBackward() {
        var current: Node = tail!!
        while (current != null) {
            print(current.data.toString() + " ")
            current = current.prev!!
        }
    }
}
