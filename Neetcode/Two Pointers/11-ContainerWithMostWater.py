from typing import List
import math


class Solution:
  def maxArea(self, height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    res = 0
    while l < r:
      area = min(height[l], height[r]) * (r - l)

      if area > res:
        res = area

      if height[l] >= height[r]:
        r -= 1
      elif height[l] < height[r]:
        l += 1

    return res


# 1 8
Solution = Solution()
print(Solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  #
print(Solution.maxArea([1, 2, 1]))
# print(Solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
