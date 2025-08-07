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

    if p and not q or not p and q:
      return False

    if p.val != q.val:
      return False

    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if root == None:
      return False
    if self.isSameTree(root, subRoot):
      return True

    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# subRoot
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

# root
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(0)

Solution = Solution()
Solution.isSubtree(root, subRoot)
