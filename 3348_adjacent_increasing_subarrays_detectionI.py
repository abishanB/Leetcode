from typing import List


class Solution:
  def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
    dp = [1] * len(nums)

    longestSubArr = 1
    for i in range(1, len(nums)):
      if longestSubArr >= k * 2:
        return True
      if nums[i] > nums[i - 1]:
        longestSubArr += 1
      else:
        longestSubArr = 1
      dp[i] = longestSubArr

    for j in range(len(dp)):
      if dp[j] >= k:
        nextSubArrayIndex = j + k
        if nextSubArrayIndex < len(dp) and dp[nextSubArrayIndex] >= k:
          return True
    return False
