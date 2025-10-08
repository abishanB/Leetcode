from typing import List
import math


class Solution:
  def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

    minPair = []
    for i in potions:
      minSpell = math.ceil(success / i)
      minPair.append(minSpell)
    minPair.sort()

    def bs(s):  # binarySearch, return max index with the maximum value <= s
      l, r = 0, len(minPair) - 1
      ans = -1
      while l <= r:
        m = (l + r) // 2
        if minPair[m] <= s:
          ans = m
          l = m + 1
        else:
          r = m - 1
      return ans

    res = []
    for s in spells:
      res.append(bs(s) + 1)
    return res
