'''
Very different here
Resort to a normal tree traversal here to search for the 2 nodes here,
 Once we reach the desired nodes p and q, we can backtrack and find the lowest common ancestor.

 When u see either node p or q:
    return some boolean flag -> lets u know if required node is ofund here

 When u see either

 Check out the code below here

                3
              /   \
            5        1                  Using the struct here
          /  \       / \                p=5, q= 1   parent = 3
         6   2       0   8
            / \                     p =5 , q = 4 return 5
           7   4                    p =2, q= 7 return 4

           # bible commentary here

   1. If the node is null,
        reached the leaf node and have not found either of the 2 values,
        return null, neight p nor q pass through here

    2. If cur value is p or q
            - cur node part of the path to 1 of the target nodes, so return it here

    3. Otherwise:
        3.1: if a node has 1 child that's null the other non-null here
            return the non-null child here

    4. If both children return non-null nodes,
            it means the current node is the lowest common ancestor, and so it is returned.

    5.And then here if both children return null as indicated here
'''


def lowestCommonAncestor(r, p, q):

    if not r:
        return None

    if r == p or r == q:
        return r
    # and then using the code here you get something a lot better
    left = lowestCommonAncestor(r.l, p, q)
    right = lowestCommonAncestor(r.r, p, q)
    if left and right:
        return r

    else:
        return left or right











