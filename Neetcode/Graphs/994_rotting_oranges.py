from typing import List
from collections import deque


class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ROWS, COLS = len(grid), len(grid[0])
    q = deque()
    freshCount = 0

    for i in range(ROWS):
      for j in range(COLS):
        if grid[i][j] == 1:
          freshCount += 1

        elif grid[i][j] == 2:
          q.append((i, j))

    res = 0  # time in minutes
    while freshCount > 0 and q:
      res += 1

      for i in range(len(q)):
        r, c = q.popleft()
        for dr, dc in directions:
          nr, nc = dr + r, dc + c
          if (nr < 0 or nc < 0 or nr >= ROWS or
                  nc >= COLS or grid[nr][nc] == 0 or grid[nr][nc] == 2
                  ):
            continue
          grid[nr][nc] = 2
          freshCount -= 1
          q.append((nr, nc))

    return res if freshCount == 0 else -1
