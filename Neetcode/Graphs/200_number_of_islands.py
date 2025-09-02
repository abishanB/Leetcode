from typing import List


class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    visited = set()
    ROWS, COLS = len(grid), len(grid[0])
    res = 0

    def search(i, j):
      if i == ROWS or j == COLS or i < 0 or j < 0 or (i, j) in visited:
        return
      visited.add((i, j))
      if grid[i][j] == "1":
        search(i + 1, j)
        search(i, j + 1)
        search(i - 1, j)
        search(i, j - 1)

    for i in range(ROWS):
      for j in range(COLS):
        if (i, j) not in visited and grid[i][j] == "1":
          search(i, j)
          res += 1

    return res
