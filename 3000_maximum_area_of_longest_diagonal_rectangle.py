from typing import List

from math import sqrt


class Solution:
  def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
    maxArea = 0
    maxDiag = 0

    for (l, w) in dimensions:
      diag = l * l + w * w
      if diag > maxDiag:
        maxArea = l * w
        maxDiag = diag
      elif diag == maxDiag and l * w > maxArea:
        maxArea = l * w
    return maxArea
