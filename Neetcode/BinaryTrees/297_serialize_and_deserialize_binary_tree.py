from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Codec:

  def serialize(self, root):

    res = [""]
    stack = []

    def dfs(root):
      if not root:
        res[0] += "*"
        return
      res[0] += "#"
      res[0] += str(root.val)
      stack.append(root)
      dfs(root.left)
      dfs(root.right)
    dfs(root)

    return res

  def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """


codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(6)
print(codec.serialize(root))
