from typing import List

import math


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
      middle = (l + r) // 2
      if target == nums[middle]:
        return middle

      # left portion
      if nums[l] <= nums[middle]:
        if target > nums[middle] or target < nums[l]:
          l = middle + 1
        else:
          r = middle - 1
      else:  # right portion
        if target < nums[middle] or target > nums[r]:
          r = middle - 1
        else:
          l = middle + 1

    return -1


Solution = Solution()
# print(Solution.search([1, 6, 10, 19, 31, 38, 44, 52, 57, 61, 73], 31))
print(Solution.search([4, 5, 6, 7, 0, 1, 2], 0))  # Original
print(Solution.search([2, 4, 5, 6, 7, 0, 1], 0))  # Rotated 1 time
print(Solution.search([1, 2, 4, 5, 6, 7, 0], 0))  # Rotated 2 times
print(Solution.search([0, 1, 2, 4, 5, 6, 7], 0))  # Rotated 3 times
print(Solution.search([7, 0, 1, 2, 4, 5, 6], 0))  # Rotated 4 times
print(Solution.search([6, 7, 0, 1, 2, 4, 5], 0))  # Rotated 5 times
print(Solution.search([5, 6, 7, 0, 1, 2, 4], 0))  # Rotated 6 times


print(Solution.search([3, 5, 1], 3))
