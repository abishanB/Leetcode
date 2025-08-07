from typing import Optional
from typing import List


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    res = [root.val]

    def dfs(root):  # max path without splitting
      if not root:
        return 0
      leftMax = dfs(root.left)
      rightMax = dfs(root.right)
      leftMax = max(leftMax, 0)
      rightMax = max(rightMax, 0)

      res[0] = max(res[0], root.val + leftMax + rightMax)
      return root.val + max(leftMax, rightMax)
    dfs(root)
    return res[0]


root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(-1)
root.right.right = TreeNode(-2)

Solution = Solution()
print(Solution.maxPathSum(root))
