package LinkedList


// Here are the templates here and then sth interesting will then happen
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