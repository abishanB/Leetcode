from typing import List


class Solution:
  def canJump(self, nums: List[int]) -> bool:
    nextJump = len(nums) - 1  # next index that jump can be made
    for i in range(len(nums) - 2, -1, -1):
      if i + nums[i] >= nextJump:
        nextJump = i

    return nextJump == 0
