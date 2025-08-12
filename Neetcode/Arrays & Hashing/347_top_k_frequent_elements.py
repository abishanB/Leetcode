from typing import List


class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = dict()
    # the index of each list tells you the frequency of the numbers in that list
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:  # count the frequency of each number
      count[n] = 1 + count.get(n, 0)

    for n, c in count.items():  # add numbers to list correpsonding to freq
      freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):  # iterate backwords through freq list
      for n in freq[i]:
        res.append(n)
        if len(res) == k:
          return res


Solution = Solution()

print(Solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(Solution.topKFrequent([1], 1))
