from typing import List


class Solution:
  def largestPerimeter(self, nums: List[int]) -> int:  # optimal solution
    nums.sort()

    for i in range(len(nums) - 1, 1, -1):
      if nums[i - 2] + nums[i - 1] > nums[i]:
        return nums[i - 2] + nums[i - 1] + nums[i]
    return 0

  def largestPerimeter1(self, nums: List[int]) -> int:  # my solution
    nums.sort()
    a, b, c = 0, 1, 2
    res = 0
    while c < len(nums):
      s1, s2, s3 = nums[a], nums[b], nums[c]
      if s1 + s2 > s3 and s1 + s3 > s2 and s3 + s2 > s1:
        res = max(res, s1 + s2 + s3)
      a += 1
      b += 1
      c += 1
    return res
