from typing import List


class Solution:
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    def backtrack(start, current):
      res.append(list(current))

      for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
          continue

        current.append(nums[i])
        backtrack(i + 1, current)  # include current value
        current.pop()  # dont include current val but cycle till next unique val
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
          i += 1
    res = []
    nums.sort()
    backtrack(0, [])

    return res


Solution = Solution()
print(Solution.subsetsWithDup([4, 4, 4, 1, 4]))
