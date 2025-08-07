from typing import Optional
from typing import List


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def fun(root, l, u):
      if root == None:
        return True

      if not (root.val < u and root.val > l):
        return False

      return fun(root.left, l, root.val) and fun(root.right, root.val, u)

    return fun(root, float("-inf"), float("inf"))
