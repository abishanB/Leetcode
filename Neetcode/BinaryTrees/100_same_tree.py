from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:  # both None
      return True

    if not p and not q or not p and q:  # either one is None but not both
      return False

    if p.val != q.val:
      return False

    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
