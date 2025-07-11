from typing import List


class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)
    longestSeq = 0
    for n in numSet:
      if (n - 1) not in numSet:

        currentSeq = 0
        while (n + currentSeq) in numSet:
          currentSeq += 1

        longestSeq = max(longestSeq, currentSeq)

    return longestSeq
