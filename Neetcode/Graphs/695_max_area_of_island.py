from typing import List
from collections import deque


class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    res = 0
    visited = set()
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def bfs(i, j):
      q = deque()
      visited.add((i, j))
      q.append((i, j))
      area = 0
      while q:
        row, col = q.popleft()
        area += 1

        for dr, dc in directions:
          nr, nc = dr + row, dc + col
          if (nr < 0 or nc < 0 or nr >= ROWS or
                      nc >= COLS or grid[nr][nc] == 0 or (nr, nc) in visited
                  ):
            continue
          q.append((nr, nc))
          visited.add((nr, nc))

      return area

    for i in range(ROWS):
      for j in range(COLS):
        if (i, j) not in visited and grid[i][j] == 1:
          res = max(res, bfs(i, j))

    return res
