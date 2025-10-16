from typing import List
from collections import Counter


class Solution:
  # n log n
  def findSmallestInteger(self, nums: List[int], value: int) -> int:

    seen = {}

    for i in range(len(nums)):
      r = nums[i] % value
      if r not in seen:
        seen[r] = r
      else:
        seen[r] = seen[r] + value

      nums[i] = seen[r]

    nums.sort()

    if nums[0] != 0:
      return 0
    for i in range(0, len(nums) - 1):
      if nums[i] + 1 != nums[i + 1]:
        return nums[i] + 1
    return nums[-1] + 1
