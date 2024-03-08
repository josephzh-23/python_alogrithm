
/*
When removing
1. Remove the value from the least used frequency value of the table and then also
from the frequency table here
 */
internal class LFUCache(var maxCapcity: Int) {
    // Frequency and the node
    var keyMap: MutableMap<Int, ListNode?> = HashMap()

    // Frequency and the list containing nodes that has the frequency there
    var freqMap: MutableMap<Int, DoublyList?> = HashMap()
    var curCapcity = 0
    private fun getNode(key: Int): ListNode? {
        if (!keyMap.containsKey(key)) return null
        // Retrive current node
        val curNode = keyMap[key]


        val list = freqMap[curNode!!.freq]
        list!!.deleteNode(key)

        // Update the freq of current node
        curNode.freq++

        /*
        Add curNode onto a higher freq list,
        frequency  |  DL
        1          | head -1- tail

        updated to
        frequnecy | DL
        2         | head -1- tail
         */
        if (!freqMap.containsKey(curNode.freq)) {
            freqMap[curNode.freq] = DoublyList()
        }
        freqMap[curNode.freq]!!.addNode(curNode)
        return curNode
    }

    operator fun get(key: Int): Int {
        if (!keyMap.containsKey(key)) return -1
        // Retrive current node from current freq list
        val curNode = getNode(key)
        return curNode!!.`val`
    }

    fun put(key: Int, value: Int) {
        if (maxCapcity == 0) return
        // Update value
        if (keyMap.containsKey(key)) {
            // Retrive current node from current freq list
            val curNode = getNode(key)
            curNode!!.`val` = value
        } else {
            // Insert value (maybe adjust the size)
            if (curCapcity == maxCapcity) {
                var lowestFreq = Int.MAX_VALUE
                for (freq in freqMap.keys) {
                    if (freqMap[freq]!!.map.isEmpty()) continue

                    // Find the lowest frequency here
                    lowestFreq = Math.min(lowestFreq, freq)
                }
                val list = freqMap[lowestFreq]
                val curNode = list!!.deleteHead()
                keyMap.remove(curNode!!.key)
                curCapcity--
            }
            val curFreq = 1
            val curNode = ListNode(value, key)
            keyMap[key] = curNode
            if (!freqMap.containsKey(curFreq)) {
                freqMap[curFreq] = DoublyList()
            }
            freqMap[curFreq]!!.addNode(curNode)
            curCapcity++
        }
    }
}

internal class ListNode {
    var prev: ListNode? = null
    var next: ListNode? = null
    var `val` = 0
    var key = 0
    var freq = 0

    constructor()
    constructor(`val`: Int, key: Int) {
        this.`val` = `val`
        this.key = key
        freq = 1
    }
}

internal class DoublyList {
    // A map with all the values and its node
    var map: MutableMap<Int, ListNode?> = HashMap()
    var head: ListNode
    var tail: ListNode

    init {
        head = ListNode()
        tail = ListNode()
        // Get them to point to each other
        tail.prev = head
        head.next = tail
    }

    fun addNode(curNode: ListNode?) {

        // head -  cur - tail
        val tailPrev = tail.prev
        tailPrev!!.next = curNode
        curNode!!.prev = tailPrev
        tail.prev = curNode
        curNode.next = tail
        // Insert this into the table now
        map[curNode.key] = curNode
    }

    fun deleteNode(key: Int): ListNode? {
        if (!map.containsKey(key)) return null
        val curNode = map[key]
        val prevNode = curNode!!.prev
        val nextNode = curNode.next
        prevNode!!.next = nextNode
        nextNode!!.prev = prevNode
        map.remove(key)
        return curNode
    }

    fun deleteHead(): ListNode? {
        if (head.next === tail) return null
        val firstNode = head.next
        return deleteNode(firstNode!!.key)
    }
}