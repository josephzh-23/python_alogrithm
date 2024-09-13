package Tree.Top6


/*
O(n)    o(n)
 */
fun connect(r: Node?): Node? {
    if (r == null) {
        return null
    }
    var head = r

    /*
    We need the next level to start from 2 - 3 and then what
    else
     */
    while (head != null) {
        var dummy = Node(0)
        var temp = dummy
        while (head != null) {


            head.left?.let {
                temp.next = it
                if(temp.next!=null){
                    temp = temp.next!!
                }
            }
            head.right?.let {
                temp.next = it
                if(temp.next!=null){
                    temp = temp.next!!
                }
            }
            // this moves from 2 -> 3-> next
            head = head.next
        }

        head = dummy.next
    }
    return r
}


fun main(){
    var root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left!!.left = Node(4)
    root.left!!.right = Node(4)

    root.right!!.right = Node(7)
    connect(root)

}

