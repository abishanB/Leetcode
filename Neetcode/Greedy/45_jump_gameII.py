from typing import List


class Solution:
  def jump(self, nums: List[int]) -> int:  # my solution O(n^2)
    dp = [0] * len(nums)

    for i in range(len(nums) - 2, -1, -1):
      if nums[i] == 0:
        dp[i] = 9999999999
        continue
      minStep = float('inf')
      for j in range(i + 1, i + nums[i] + 1):
        if j >= len(nums):
          break
        if j == len(nums) - 1:
          minStep = 0
          break
        minStep = min(minStep, dp[j])
      dp[i] = 1 + minStep
    return dp[0]

  def jump(self, nums: List[int]) -> int:  # bfs optimal solution O(n)
    res = 0
    l, r = 0, 0
    while r < len(nums) - 1:
      farthest = 0
      for i in range(l, r + 1):
        farthest = max(farthest, i + nums[i])
      l = r + 1
      r = farthest
      res += 1
    return res


Solution = Solution()
print(Solution.jump([1, 2, 3]))
