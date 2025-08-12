from typing import Optional
from typing import List
import collections


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []

    q = []
    q.append(root)

    while q:
      qLen = len(q)
      level = []
      for i in range(qLen):
        node = q.pop(0)
        if node:
          level.append(node.val)
          q.append(node.left)
          q.append(node.right)

      if level:
        res.append(level)

    return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

Solution = Solution()
print(Solution.levelOrder(root))
