class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val):
      return root

    if p == root or q == root:
      return root

    if p.val > root.val:  # this also means q is greater
      return self.lowestCommonAncestor(root.right, p, q)
    # p is less than root
    return self.lowestCommonAncestor(root.left, p, q)


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

Solution = Solution()
print(Solution.lowestCommonAncestor(root, 2, 8))
