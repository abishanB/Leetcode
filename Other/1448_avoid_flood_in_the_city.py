from typing import List
from sortedcontainers import SortedList


class Solution:
  def avoidFlood(self, rains: List[int]) -> List[int]:
    n = len(rains)
    res = [1] * n
    rainMap = {}
    l = SortedList()

    for i, x in enumerate(rains):
      if x == 0:
        l.add(i)
      else:
        res[i] = -1
        if x in rainMap:
          bs = l.bisect_left(rainMap[x])
          if bs == len(l):
            return []
          res[l[bs]] = x
          l.discard(l[bs])
        rainMap[x] = i
    return res
