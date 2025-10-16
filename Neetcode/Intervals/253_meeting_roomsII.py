from typing import List


class Interval(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end


class Solution:
  def minMeetingRooms(self, intervals: List[Interval]) -> int:
    start = []
    end = []

    for interval in intervals:
      start.append(interval.start)
      end.append(interval.end)
    start.sort()
    end.sort()

    startP = 0
    endP = 0
    count = 0
    res = 0
    while startP < len(intervals) and endP < len(intervals):
      if start[startP] == end[endP] or start[startP] > end[endP]:
        endP += 1
        count -= 1
      else:
        startP += 1
        count += 1
        res = max(res, count)

    return res
