
from typing import List
import heapq


class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    heap = []  # max heap
    for weight in stones:
      heapq.heappush(heap, -weight)  # invert weight for max

    while len(heap) > 1:
      heaviest1 = heapq.heappop(heap)
      heaviest2 = heapq.heappop(heap)

      if -heaviest1 > heaviest2:
        heapq.heappush(heap, heaviest1 - heaviest2)

    if not heap:
      return 0

    return -heap[0]


Solution = Solution()
print(Solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))
