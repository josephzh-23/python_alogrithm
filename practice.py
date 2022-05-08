

# practice reverse linkedlist
cur = 5
while cur:
    next = cur.next
    cur.next = prev
    cur = cur.next


#