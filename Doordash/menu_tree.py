'''

Here then
'''
from typing import List
'''
This comes from this post here 
https://leetcode.com/discuss/post/1265810/doordash-phonescreen-by-abhardwaj-u7g4/


1)if key is not found in hashmap, count++
2) if value of Node changed, count++
3) if active status is changed, count++

and return count.
Time complexity: O(N+M) where N is number of nodes in new menu and M is number of nodes in old menu. This comes from two BFS/DFS performed.
Space complexity: O(N+M) because of DFS stack or BFS queue and also hashmap used which is O(N)

'''

class Node:
    def __init__(self, key: str, value: int, active: bool):
        self.key = key
        self.value = value
        self.active = active
        self.children = []

    def equals(self, node: 'Node'):
        if node is None:
            return False

        return (self.key == node.key and
                self.value == node.value and
                self.active == node.active)


def get_modified_items(oldMenu, newMenu):

    if oldMenu is None and newMenu is None:
        return 0

    count = 0

    '''
    Only if they are the same then we keep going here, this is very important here 
    '''
    if oldMenu is None or newMenu is None or not oldMenu.equals(newMenu):
        count += 1

    child1 = fillMapWithChildNodes(oldMenu)
    child2 = fillMapWithChildNodes(newMenu)
    '''
    
    '''

    print("child1 keys are ", child1.keys)
    for k in child1.keys():
        count += get_modified_items(child1.get(k), child2.get(k))

    print("child2 keys are ", child2.keys)

    for k in child2.keys():
        if k not in child1:
            count += get_modified_items(None, child2.get(k))

    return count


def fillMapWithChildNodes(menu: 'Node'):
    m = {}
    if menu is None:
        return m
    '''
    a.children.append(b)
    
    a's child : b, c
    
    as said here 
    m[b] = Node("b", 2, True)
    '''
    for node in menu.children:
        print("the node key is", node.key)
        m[node.key] = node

    return m


'''
         Existing tree
            a(1, T)
          /         \
        b(2, T)   c(3, T)
      /       \
  d(4, T) e(5, T)

                New tree
                a(1, T)
             /          \
       b(2, T)         c(3, T)
      /                   \
 d(4, T)                   e(5, T)

'''

a = Node("a", 1, True)
b = Node("b", 2, True)
c = Node("c", 3, True)
d = Node("d", 4, True)
e = Node("e", 5, True)
g = Node("g", 7, True)

a.children.append(b)
a.children.append(c)

# note here added for b and
b.children.append(d)
b.children.append(e)
# c.children.append(g)

a1 = Node("a", 1, True)
b1 = Node("b", 2, True)
c1 = Node("c", 3, True)
d1 = Node("d", 4, True)
e1 = Node("e", 5, True)
f1 = Node("f", 6, True)
g1 = Node("g", 7, False)


a1.children.append(b1)
a1.children.append(c1)

b1.children.append(d1)
c1.children.append(e1)

count = get_modified_items(a, a1)
print("changed items are", count)

