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
  def reorderList(self, head: Optional[ListNode]) -> None:
    slow, fast = head, head.next

    # find middle
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    # reverse 2nd half
    second = slow.next
    slow.next = None
    prev = None
    while second:
      tmp = second.next
      second.next = prev
      prev = second
      second = tmp

    # merge both lists by alternatig
    first, second = head, prev

    while second:  # 2nd half is either shorter or same size as first
      tmp1, tmp2 = first.next, second.next
      first.next = second
      second.next = tmp1
      first, second = tmp1, tmp2


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)


# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

Solution = Solution()
print_list(node1)

print_list(Solution.reorderList(node1))
