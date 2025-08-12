from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def print_list(head):
  current = head
  while current:
    print(f"{current.val} -> ", end="")
    current = current.next
  print("None")


class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    l = dummy
    r = head
    while n > 0 and r:
      r = r.next
      n -= 1

    while r:
      l = l.next
      r = r.next

    l.next = l.next.next
    return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)


# Link nodes
node1.next = node2
node2.next = None
node3.next = node4
node4.next = node5

Solution = Solution()
print_list(node1)
print_list(Solution.removeNthFromEnd(node1, 2))
