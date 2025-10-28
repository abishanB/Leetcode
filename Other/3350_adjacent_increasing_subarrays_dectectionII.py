from typing import List


class Solution:
  def maxIncreasingSubarrays(self, nums: List[int]) -> int:  # O(n)
    dp = [1] * len(nums)

    longestSubArr = 1
    res = 1
    for i in range(1, len(nums)):
      if nums[i] > nums[i - 1]:
        longestSubArr += 1
      else:
        longestSubArr = 1
      dp[i] = longestSubArr
      res = max(res, longestSubArr // 2)
      if longestSubArr > res:
        lastSubArrayIndex = i - longestSubArr
        if lastSubArrayIndex >= 0 and dp[lastSubArrayIndex] > res:
          res = min(dp[i], dp[lastSubArrayIndex])
    return res
