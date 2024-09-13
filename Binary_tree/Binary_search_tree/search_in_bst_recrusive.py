'''

A new function here that's useful here
O(h)
'''

def search(r, key):

    if r is None or r.key == key:
        return r

    # if key is greater than r's key here

    if r.key < key:
        return search(r.right, key)

    # the key is smaller here
    return search(r.left, key)















