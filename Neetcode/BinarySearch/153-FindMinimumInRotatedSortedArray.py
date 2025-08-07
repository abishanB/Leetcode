from typing import List

import math


class Solution:
  def findMin(self, nums: List[int]) -> int:
    if len(nums) <= 3:
      return min(nums)
    if nums[0] < nums[-1]:
      return nums[0]

    middle = math.floor(len(nums) / 2)

    if nums[middle] < nums[middle - 1]:
      return nums[middle]

    if nums[middle] > nums[middle + 1]:
      return nums[middle + 1]

    if nums[middle] > nums[0]:
      return self.findMin(nums[middle + 1:])

    if nums[middle] < nums[0]:
      return self.findMin(nums[:middle])


Solution = Solution()
print(Solution.findMin([3, 4, 5, 1, 2]))
print(Solution.findMin([4, 5, 6, 7, 0, 1, 2]))
print(Solution.findMin([11, 13, 15, 17]))
print(Solution.findMin([44, 52, 57, 61, 73, 1, 6, 10, 19, 31, 38]))
print(Solution.findMin([38, 44, 52, 57, 61, 73, 1, 6, 10, 19, 31]))
print(Solution.findMin([31, 38, 44, 52, 57, 61, 73, 1, 6, 10, 19]))
print(Solution.findMin([1, 6, 10, 19, 31, 38, 44, 52, 57, 61, 73]))


# [44, 52, 57, 61, 73, 1, 6, 10, 19, 31, 38]

# [38, 44, 52, 57, 61, 73, 1, 6, 10, 19, 31]

# [31, 38, 44, 52, 57, 61, 73, 1, 6, 10, 19]
