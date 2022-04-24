from Binary_Search_Tree.BSTNode import Node

'''
This is a prebuilt tree available for use anywhere
'''


class BSTree:
  def __init__(self):
    self.root = Node()

    # Creating 2nd level:
    one = Node()
    two = Node()
    self.root.left = one
    self.root.right = Node()

    # Creating 3rd level:
    three = Node()
    four = Node()
    five = Node()
    one.left = three
    two.left = four
    two.right = five

  def findMax(self, a, b):
    if a >= b:
      return a;
    else:
      return b;

  def getHeight(self, root):
    # Base case:
    if root is None:
      return 0;

    return self.findMax(self.getHeight(root.left), self.getHeight(root.right)) + 1;
