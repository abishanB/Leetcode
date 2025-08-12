from typing import List


class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    uniqueNums = set()
    for num in nums:
      if num in uniqueNums:
        return True
      uniqueNums.add(num)
    return False


Solution = Solution()
print(Solution.containsDuplicate([1, 2, 3, 1]))
print(Solution.containsDuplicate([1, 2, 3, 4]))
