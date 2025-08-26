from typing import List


class TrieNode:
  def __init__(self):
    self.children = {}
    self.word = None

  def insert(self, word: str) -> None:
    curr = self
    for c in word:
      if c not in curr.children:
        curr.children[c] = TrieNode()
      curr = curr.children[c]

    curr.word = word


class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()
    for w in words:
      root.insert(w)

    ROWS, COLS = len(board), len(board[0])
    res = []

    def dfs(r, c, node):
      char = board[r][c]
      if char not in node.children:
        return

      nxt = node.children[char]
      if nxt.word:
        res.append(nxt.word)
        nxt.word = None

      board[r][c] = "#"
      for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
          dfs(nr, nc, nxt)
      board[r][c] = char

      if not nxt.children:
        node.children.pop(char)

    for r in range(ROWS):
      for c in range(COLS):
        dfs(r, c, root)

    return res
