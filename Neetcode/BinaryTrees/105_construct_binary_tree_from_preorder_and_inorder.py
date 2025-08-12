from typing import Optional
from typing import List


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
      return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
    root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
    return root


Solution = Solution()
# print(Solution.buildTree([4, 2, 1, 3, 5], [1, 2, 3, 4, 5]))
print(Solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
# print(Solution.buildTree([-1], [-1]).val)
