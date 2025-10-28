from collections import defaultdict
from typing import List


class Solution:
  def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
    counts = defaultdict(int)
    blacks = set(map(tuple, coordinates))

    for x, y in blacks:
      # this black cell contributes to up to 4 blocks
      for dx, dy in [(0, 0), (-1, 0), (0, -1), (-1, -1)]:
        i, j = x + dx, y + dy
        # (i,j) is top-left corner of a 2x2 block
        if 0 <= i < m - 1 and 0 <= j < n - 1:
          counts[(i, j)] += 1

    res = [0] * 5
    for c in counts.values():
      res[c] += 1

    total_blocks = (m - 1) * (n - 1)
    res[0] = total_blocks - sum(res)
    return res
