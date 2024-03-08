package LinkedList

fun printLinkedList(head: ListNode?){
    var temp = head

    while(temp!=null){
        println(temp.value)
        temp= temp.next
    }
}