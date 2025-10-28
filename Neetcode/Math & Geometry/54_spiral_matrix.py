from typing import List


class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    currDirection = 0

    res = []
    path = set()
    i = 0
    j = 0

    total = (len(matrix) * len(matrix[0]))
    while len(res) != total:
      res.append(matrix[i][j])
      path.add((i, j))
      iNext = i + directions[currDirection][0]
      jNext = j + directions[currDirection][1]
      if iNext < 0 or iNext == len(matrix) or jNext < 0 or jNext == len(matrix[0]) or (iNext, jNext) in path:
        currDirection += 1
        if currDirection == 4:
          currDirection = 0
        i += directions[currDirection][0]
        j += directions[currDirection][1]
      else:
        i = iNext
        j = jNext
    return res
