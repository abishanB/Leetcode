from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  # iterative
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
      nxt = curr.next
      curr.next = prev
      prev = curr
      curr = nxt
    return prev

  # recursive
  def reverseListRecurse(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return None

    newHead = head

    if head.next:
      newHead = self.reverseListRecurse(head.next)
      head.next.next = head
    head.next = None

    return newHead
