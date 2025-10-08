from typing import List


class Solution:  # my solution: n log n
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    res = []
    new = [-1, -1]
    for i in range(len(intervals)):
      if new == [-1, -1]:
        new = intervals[i]
        continue

      if new[1] >= intervals[i][0]:
        new[1] = max(new[1], intervals[i][1])
      else:
        res.append(new)
        new = intervals[i]
    if new != [-1, -1]:
      res.append(new)
    return res
