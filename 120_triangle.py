from typing import List


class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:  # optimal solution
    for i in range(1, len(triangle)):
      for j in range(len(triangle[i])):
        if j == 0:
          triangle[i][j] += triangle[i - 1][0]
        elif j == len(triangle[i]) - 1:
          triangle[i][j] += triangle[i - 1][-1]
        else:
          triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])

    return min(triangle[-1])

  def minimumTotal1(self, triangle: List[List[int]]) -> int:  # my solution
    seen = dict()

    def dfs(i, j):  # i - level, j pos on level
      if i == len(triangle) or j == len(triangle[i]):
        return 0

      if (i, j) in seen:
        return triangle[i][j] + seen[(i, j)]
      below = dfs(i + 1, j)
      belowRight = dfs(i + 1, j + 1)
      seen[(i, j)] = min(below, belowRight)

      return triangle[i][j] + min(below, belowRight)

    return dfs(0, 0)
