from collections import deque

from Binary_Search_Tree.BSTNode import insert, Node
from Binary_Search_Tree.breath_first_search_rec import printLevelOrderIter


class MyStack:

    def __init__(s):
        s.q = deque()

    def push(s, x):
        s.q.append(x)