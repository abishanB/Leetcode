# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    l1_copy = l1
    l2_copy = l2
    while l1_copy and l2_copy:  # make both lists of equal length by adding 0s
      if l1_copy.next and not l2_copy.next:
        l2_copy.next = ListNode()
      elif not l1.next and l2.next:
        l1_copy.next = ListNode()
      l1_copy = l1_copy.next
      l2_copy = l2_copy.next

    head = ListNode()
    curr = head
    carry = 0
    while l1 or l2:
      s = l1.val + l2.val + carry
      if s >= 10:
        carry = 1
        s = s % 10
      else:
        carry = 0

      curr.val = s
      if l1.next or l2.next:
        curr.next = ListNode()
        curr = curr.next
      l1 = l1.next
      l2 = l2.next

    if carry > 0:
      curr.next = ListNode(carry)
    return head
