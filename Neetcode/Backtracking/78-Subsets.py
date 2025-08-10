from typing import List


class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:

    def backtrack(start, current):
      res.append(list(current))

      for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
          continue

        current.append(nums[i])

        backtrack(i + 1, current)
        current.pop()
    res = []
    backtrack(0, [])
    nums.sort()
    return


Solution = Solution()
print(Solution.subsets([1, 2, 3]))
