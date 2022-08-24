def inOrder(r, list):

    global prev, count, max
    inOrder(r.left, list)

    if prev:
        if prev.val == r.val:
            count+=1
        else:
            count = 1

    if count > max:
        list.clear()
        list.append(r.val)
        max = count

    if count == max:
        list.append(r.val)

    prev = r
    print('the value of prev is ', prev.val)
    inOrder(r.right, list)
