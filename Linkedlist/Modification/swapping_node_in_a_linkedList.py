'''




'''
from palindrome_linkedlist import ListNode


def make_list(elements):
   head = ListNode(elements[0])
   for element in elements[1:]:
      ptr = head
      while ptr.next:
         ptr = ptr.next
      ptr.next = ListNode(element)
   return head

def print_list(head):
   ptr = head
   print('[', end = "")
   while ptr:
      print(ptr.val, end = ", ")
      ptr = ptr.next
   print(']')
def solve(L, k):
   temp = L
   for i in range(k-1):
      temp = temp.next
   firstNode = temp
   secondNode = L

   print("first and 2nd nodes are ", firstNode.data, secondNode.data)
   while temp.next:
      secondNode = secondNode.next
      temp = temp.next
   firstNode.data , secondNode.data = secondNode.data , firstNode.data
   return L

L = [1,5,6,7,1,6,3,9,12]
k = 3
print_list(solve(make_list(L), k))
