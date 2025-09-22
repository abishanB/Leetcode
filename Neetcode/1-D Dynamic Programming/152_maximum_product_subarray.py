from typing import List


class Solution:
  def maxProduct(self, nums: List[int]) -> int:  # my solutions

    minP = [None] * len(nums)
    minP[-1] = nums[-1]
    maxP = [None] * len(nums)
    maxP[-1] = nums[-1]
    res = nums[-1]

    for i in range(len(nums) - 2, -1, -1):
      minP[i] = min(nums[i] * minP[i + 1], nums[i] * maxP[i + 1], nums[i])
      maxP[i] = max(nums[i] * minP[i + 1], nums[i] * maxP[i + 1], nums[i])
      res = max(minP[i], maxP[i], res)
    return res

  def maxProduct1(self, nums: List[int]) -> int:  # neetcode solution
    res = nums[0]
    curMin, curMax = 1, 1

    for num in nums:
      tmp = curMax * num
      curMax = max(num * curMax, num * curMin, num)
      curMin = min(tmp, num * curMin, num)
      res = max(res, curMax)
    return res
