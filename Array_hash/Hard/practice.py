def mergeTwoArray(a1, m, a2, n):

    # no extra mem

    last = m+ n - 1
    while m> 0 and n>0:
        # WHile both bigger than 0
        if a1[m-1 ] > a2[n-1]:
            a1[last] = a1[m-1]
            m-=1

        # in the other case
        else:
            a1[last] = a2[n-1]
            n-=1
        last-=1

    while n> 0:
        a1[last] = a2[n-1]
        n-=1
        last-=1