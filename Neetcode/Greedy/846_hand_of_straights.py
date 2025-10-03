from typing import List
from collections import Counter


class Solution:
  def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
      return False

    if groupSize == 1:
      return True

    counts = dict()

    for n in hand:
      counts[n] = 1 + counts.get(n, 0)
    hand.sort()

    for n in hand:
      if not counts[n]:
        continue
      for i in range(n, n + groupSize):
        if i not in counts or not counts[i]:
          return False
        counts[i] -= 1

    return True


Solution = Solution()
print(Solution.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
