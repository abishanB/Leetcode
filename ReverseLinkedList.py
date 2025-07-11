from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def printLinkedList(lst: Optional[ListNode]) -> Optional[ListNode]:
  print(lst.val, end=" ")
  nextNode = lst.next
  while nextNode != None:
    print(nextNode.val, end=" ")
    nextNode = nextNode.next
  print()


def reverseLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
  prev = None
  current = head

  while current:
    next_node = current.next  # Store next node
    current.next = prev       # Reverse the link
    prev = current            # Move prev forward
    current = next_node       # Move current forward

  return prev  # New head of the reversed list


l1 = ListNode(2, ListNode(4, ListNode(3, None)))
printLinkedList(l1)
printLinkedList(reverseLinkedList(l1))
