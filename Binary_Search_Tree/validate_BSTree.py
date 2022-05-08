import math


def isValidBST(root):

    s= []
    leftChildVal = -math.inf

    while s or root is not None:
