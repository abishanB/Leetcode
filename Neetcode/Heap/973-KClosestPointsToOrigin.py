from typing import List
import heapq


class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    heap = []  # minHeap
    for p in points:
      dist = p[0] * p[0] + p[1] * p[1]
      heap.append((dist, p))

    heapq.heapify(heap)
    res = []

    for i in range(k):
      res.append(heapq.heappop(heap)[1])
    return res


Solution = Solution()
# print(Solution.kClosest([[1, 3], [-2, 2]], 1))
# print(Solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
# print(Solution.kClosest([[0, 1], [1, 0]], 2))
print(Solution.kClosest([[2, 2], [2, 2], [3, 3], [2, -2], [1, 1]], 4))
