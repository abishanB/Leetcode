from typing import List


class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()

    def dfs(i, curr, total):
      if total == target:
        res.append(curr[:])
        return

      if i >= len(candidates) or total > target:
        return

      curr.append(candidates[i])
      dfs(i + 1, curr, total + candidates[i])
      curr.pop()
      i += 1
      while i < len(candidates) and candidates[i] == candidates[i - 1]:
        i += 1
      dfs(i, curr, total)

    dfs(0, [], 0)
    return res


Solution = Solution()
print(Solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(Solution.combinationSum2([2, 5, 2, 1, 2], 5))
