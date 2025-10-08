from typing import List


class Solution:
  # my solution
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if len(intervals) == 0:
      return [newInterval]
    if newInterval[0] > intervals[-1][1]:
      intervals += [newInterval]
      return intervals
    if newInterval[1] < intervals[0][0]:
      return [newInterval] + intervals
    res = []
    overlap = []
    newStart = newInterval[0]
    newEnd = newInterval[1]
    for [start, end] in intervals:
      if end < newStart or start > newEnd:
        continue
      overlap.append([start, end])

    if not overlap:
      for i, [start, end] in enumerate(intervals):
        res.append([start, end])
        if i < len(intervals) - 1 and newStart > end and newEnd < intervals[i + 1][0]:
          res.append([newStart, newEnd])
      return res

    updateStart = min(overlap[0][0], newStart)
    updateEnd = max(overlap[-1][1], newEnd)

    intervalAdded = False
    for [start, end] in intervals:
      if end < newStart or start > newEnd:
        res.append([start, end])
        continue
      if not intervalAdded:
        res.append([updateStart, updateEnd])
        intervalAdded = True

    return res


class NeetcodeSolution:  # neetocde
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []

    for i in range(len(intervals)):
      if newInterval[1] < intervals[i][0]:
        res.append(newInterval)
        return res + intervals[i:]
      elif newInterval[0] > intervals[i][1]:
        res.append(intervals[i])
      else:
        newInterval = [
            min(newInterval[0], intervals[i][0]),
            max(newInterval[1], intervals[i][1]),
        ]
    res.append(newInterval)
    return res
