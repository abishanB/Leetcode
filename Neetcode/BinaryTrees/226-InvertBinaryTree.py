from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root == None:
      return

    root.left = self.invertTree(root.left)
    root.right = self.invertTree(root.right)

    l = root.left
    r = root.right

    root.left = r
    root.right = l
    return root
