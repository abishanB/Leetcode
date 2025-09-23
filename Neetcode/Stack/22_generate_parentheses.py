from typing import List


class Solution:
  def generateParenthesis(self, n: int) -> List[str]:  # my solution
    res = []
    s = ""

    def dfs(s, stack, pairs):
      if not stack and pairs == n:
        res.append(s)
        return
      if not stack:
        dfs(s + "(", ["("], pairs)
        return
      if len(stack) + pairs < n:
        dfs(s + "(", stack + ["("], pairs)
      stack.pop()
      dfs(s + ")", stack, pairs + 1)

    dfs(s, [], 0)
    return res
