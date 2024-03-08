package LinkedList

// Here we delete all the duplicates
fun main() {
    var i = ListNode(1)

    append(i, 4)
    append(i, 4)
    append(i, 7)
    append(i, 8)
//    printLinkedList(i)

    deleteAllDups(i)
    printLinkedList(i)

}


// When deleting you must get the element before this fff
fun deleteAllDups(i: ListNode?) {
    var cur = i
    var prev: ListNode? = null
    var set = hashSetOf<Int>()

    while(cur?.next != null){

        if(set.contains(cur.value)){
            val next = cur.next
            prev?.next = next?.next
        }else{
            set.add(cur.value)
            prev = cur
        }

        cur = cur.next
    }
}
