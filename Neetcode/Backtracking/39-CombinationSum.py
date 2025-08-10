from typing import List


class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()

    def dfs(i, curr, total):
      if total == target:
        res.append(curr[:])
        return
      if i >= len(candidates) or total > target:
        return

      curr.append(candidates[i])
      dfs(i, curr, total + candidates[i])
      curr.pop()
      dfs(i + 1, curr, total)

    dfs(0, [], 0)
    return res


Solution = Solution()
print(Solution.combinationSum([2, 3, 6, 7], 7))
