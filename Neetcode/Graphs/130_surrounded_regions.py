from typing import List


class Solution:
  def optimal_solve(self, board: List[List[str]]) -> None:  # my solution
    ROWS, COLS = len(board), len(board[0])

    def capture(r, c):  # dfs
      if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
        return
      board[r][c] = "T"
      capture(r + 1, c)
      capture(r - 1, c)
      capture(r, c + 1)
      capture(r, c - 1)

    # Capture unsurrounded regions, change O to T
    for r in range(ROWS):
      if board[r][0] == "O":
        capture(r, 0)
      if board[r][COLS - 1] == "O":
        capture(r, COLS - 1)

    for c in range(COLS):
      if board[0][c] == "O":
        capture(0, c)
      if board[ROWS - 1][c] == "O":
        capture(ROWS - 1, c)

    # Change Os To Xs and Ts back to Os
    for r in range(ROWS):
      for c in range(COLS):
        if board[r][c] == "O":
          board[r][c] = "X"
        elif board[r][c] == "T":
          board[r][c] = "O"

  def solve(self, board: List[List[str]]) -> None:  # my solution
    """
    Do not return anything, modify board in-place instead.
    """
    ROWS, COLS = len(board), len(board[0])
    visited = set()
    region = set()

    def dfs(i, j):
      if (i, j) in visited:
        return True

      visited.add((i, j))
      if i < 0 or j < 0 or i == ROWS or j == COLS:
        return False

      if board[i][j] == "X":
        return True

      a, b, c, d = dfs(i + 1, j), dfs(i - 1, j), dfs(i, j + 1), dfs(i, j - 1)
      if a and b and c and d:
        region.add((i, j))
        return True
      return False

    for i in range(ROWS):
      for j in range(COLS):
        if board[i][j] == "O" and (i, j) not in visited:
          if dfs(i, j):
            for (r, c) in region:
              board[r][c] = "X"
          region = set()
