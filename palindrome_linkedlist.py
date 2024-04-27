class ListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def palindromeLinkedList(head: ListNode):
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
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(1)

print(palindromeLinkedList(l1))