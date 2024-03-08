class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def palindromeLinkedList(head: Node):
    nums = []
    while head:
        # allow traversal here
        nums.append(head.data)
        head = head.next
    return isPalindromicArray(nums)


def isPalindromicArray(arr):
    l, r = 0, len(arr) - 1
    while (l <= r):
        if (arr[l] != arr[r]):
            return False
        l += 1
        r -= 1
    return True
l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(2)
l1.next.next.next = Node(1)

print(palindromeLinkedList(l1))