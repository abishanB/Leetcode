from typing import List
import heapq


class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    heap = []  # minHeap
    for n in nums:
      if len(heap) < k:
        heapq.heappush(heap, n)
        continue

      if n > heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, n)

    return heap[0]


Solution = Solution()
print(Solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(Solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
