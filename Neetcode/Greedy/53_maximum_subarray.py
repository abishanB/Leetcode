from typing import List


class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    res, curSum = nums[0], 0
    for num in nums:
      if curSum < 0:
        curSum = 0
      curSum += num
      res = max(res, curSum)
    return res


Solution = Solution()
print(Solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
