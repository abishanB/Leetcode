from typing import List


class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    l, r = 0, len(matrix) - 1
    while l < r:
      tempR = matrix[r]
      matrix[r] = matrix[l]
      matrix[l] = tempR
      l += 1
      r -= 1

    for i in range(len(matrix)):
      for j in range(i, len(matrix)):
        temp = matrix[j][i]
        matrix[j][i] = matrix[i][j]
        matrix[i][j] = temp
