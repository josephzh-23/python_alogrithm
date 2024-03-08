package LinkedList

/*
LRU a linkedlist and a

# of keys exceed capacity

Why use doubly linkedlist
1 <-> 2
Insert node 1 first, then insert node 2

Most freq at the front, least freq at the back here

 */
internal class LRUCache(var capacity: Int) {
    var head: Node = Node(0, 0)
    var tail: Node = Node(0, 0)
    var map: MutableMap<Int, Node?> = HashMap()

    init {
        head.next = tail
        tail.prev = head
    }

    /*

    1 <-> 2
            1st item and 2nd item here if you want to get 1
        you have to switch order 1 and 2
    2 <->  1
     */
    operator fun get(key: Int): Int {
        if (map.containsKey(key)) {
            val data = map[key]
            /*
            Move the data from the back to the head here
             */
            remove(data)
            //insert it
            insert(data)
            return data!!.value
        }
        return -1
    }

    fun put(key: Int, value: Int) {
        //if value is already present we move it to top
        if (map.containsKey(key)) {
            remove(map[key])
        }
        /*
        If cache full delete the least frequently used which is at the back
        here, keep most frequently used element here

         */
        if (capacity == map.size) {
            remove(tail.prev)
        }
        //tail.prev --> least recently used
        insert(Node(key, value))
    }

    // Least recently used element first
    fun remove(node: Node?) {
        map.remove(node!!.key)
        node.prev!!.next = node.next
        node.next!!.prev = node.prev
    }

    fun insert(node: Node?) {
        map[node!!.key] = node
        val headNext = head.next
        head.next = node
        node.prev = head
        headNext!!.prev = node
        node.next = headNext
    }

    internal inner class Node(var key: Int, var value: Int) {
        var prev: Node? = null
        var next: Node? = null
    }
}

