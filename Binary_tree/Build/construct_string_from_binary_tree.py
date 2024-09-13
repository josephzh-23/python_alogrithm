from Binary_tree.BSTNode import TreeNode



'''
Case 1: 
 Both the left child and the right child exist for the current node.
 
 1. 
 put the braces () around both the left child’s preorder traversal output and the right child’s preorder traversal output.
 
Case 2: 
Both left and right child not exist 
No braces 

2 has both left and right as the child here very important 
1(2(4)(5))(3)

Case 3: 
only left child exists 

1 (2(4)) (3(5)(6))

Case  4:
only the rigth child exists in this case then here we
want the situation for () before the right one here 


and like the above here 
1 (2() (4))  (3 (5) (6))

And once we have this we have 



The iterative approach here 
1. If both the l and r exist, process r, l and r 

Why do we need the set here?

1. When a node is being processed:
    1) has not been visited, has not been popped from the stack 
    2) Will be popped form the stack when encountered again
    3) This only occurs when the preorder traversl of both l and r are done completely
    
    4) So we add ) to mark it as done here  
    
    
If a node has already been processed 
it is popped off from the stack when encountered again.


'''


def preorderIter(root):
    # Base CAse
    if root is None:
        return

    stack = [root]
    s = ""
    visited = set()
    # we add the stuff here

    while stack:
        t = stack[-1]

        print(t.val)
        if t in visited:
            stack.pop()
            s += ")"

            # not in visited
        else:
            visited.add(t)
            s += '(' + str(t.val)


            # only the right exists
            # 1 (2 () (4))  (3 (5) (6))
            if t.l is None and t.r:
                s += "()"

            if t.r:
                stack.append(t.r)

            if t.l:
                stack.append(t.l)

    print(s)

root = TreeNode(1)
root.l = TreeNode(2)
root.r = TreeNode(3)
root.l.l = TreeNode(4)
preorderIter(root)
