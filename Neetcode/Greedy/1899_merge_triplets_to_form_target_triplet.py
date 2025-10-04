from typing import List


class Solution:
  def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
    a = False
    b = False
    c = False

    for triple in triplets:
      if triple[0] == target[0] and triple[1] <= target[1] and triple[2] <= target[2]:
        a = True

      if triple[1] == target[1] and triple[0] <= target[0] and triple[2] <= target[2]:
        b = True

      if triple[2] == target[2] and triple[0] <= target[0] and triple[1] <= target[1]:
        c = True

      if a and b and c:
        return True

    return False
