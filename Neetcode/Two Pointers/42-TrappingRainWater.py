from typing import List


class Solution:
  def trap(self, height: List[int]) -> int:
    res = 0
    l = 0
    r = len(height) - 1
    maxH = 0
    ref = 0
    while l < r:
      currentHeight = min(height[l], height[r])

      if currentHeight >= maxH:
        maxH = currentHeight
        if height[l] >= height[r]:
          r -= 1
          ref = l
          continue
        ref = r
        l += 1
        continue

      if height[l] <= maxH and l != ref:
        res += maxH - height[l]
        l += 1
        continue
      if height[r] <= maxH and r != ref:
        res += maxH - height[r]
        r -= 1
        continue

    return res


Solution = Solution()


print(Solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution.trap([4, 2, 0, 3, 2, 5]))
print(Solution.trap([2, 0, 2]))
