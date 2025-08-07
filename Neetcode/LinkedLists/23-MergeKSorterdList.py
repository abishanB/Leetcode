from typing import Optional
from typing import List


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def create_linked_list(arr):
  if not arr:
    return None
  head = ListNode(arr[0])
  current = head
  for val in arr[1:]:
    current.next = ListNode(val)
    current = current.next
  return head


def print_list(head):
  current = head
  while current:
    print(f"{current.val} -> ", end="")
    current = current.next
  print("None")


class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    values = []
    for head in lists:
      while head:
        values.append(head.val)
        head = head.next

    values.sort()

    for val in values:
      tail.next = ListNode(val)
      tail = tail.next

    return dummy.next


list1 = create_linked_list([1, 4, 5])
list2 = create_linked_list([1, 3, 4])
list3 = create_linked_list([2, 6])
Solution = Solution()
print_list(Solution.mergeKLists([list1, list2, list3]))
