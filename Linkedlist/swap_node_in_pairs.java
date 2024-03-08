package LinkedList;

import LinkedList.ListNode;

public class swap_node_in_pairs {

    public ListNode swapPairs(ListNode head){
        ListNode temp = new ListNode(0);
        temp.next = head;

        ListNode cur = temp;

        while(cur.next !=null && cur.next.next!=null){
            ListNode firstNode = cur.next;
            ListNode secondNode = cur.next.next;

            // Pt 1 to 3
            firstNode.next = secondNode.next;

            // pt dummy to 2
            cur.next = secondNode;
            //  2 -> 1
            cur.next.next = firstNode;

            // mv cur to 3
            cur = cur.next;

        }
        return temp.next;
    }
}












