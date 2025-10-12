from typing import List


class Interval(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end


class Solution:
  def canAttendMeetings(self, intervals: List[Interval]) -> bool:
    newList = []
    for i in intervals:
      newList.append([i.start, i.end])
    newList.sort()
    for i in range(0, len(newList) - 1):
      if newList[i][1] > newList[i + 1][0]:
        return False
    return True
