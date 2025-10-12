from typing import List
import heapq


class Solution:
  # Dijkstra’s algorithm
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    d = {}

    for u, v, w in times:
      if u not in d:
        d[u] = []
      d[u].append([v, w])

    heap = [(0, k)]  # min heap
    visited = set()
    t = 0
    while heap:
      currTime, currNode = heapq.heappop(heap)
      if currNode in visited:
        continue
      visited.add(currNode)
      t = max(t, currTime)
      if currNode not in d:
        continue

      for v, w in d[currNode]:
        if v not in visited:
          heapq.heappush(heap, (w + currTime, v))

    return t if len(visited) == n else -1
