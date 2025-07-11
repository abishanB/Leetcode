from typing import List


class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1
    while l < r:
      if numbers[l] + numbers[r] > target:
        r -= 1
      elif numbers[l] + numbers[r] < target:
        l += 1
      else:
        return l + 1, r + 1


Solution = Solution()
# print(Solution.twoSum([2, 7, 11, 15], 9))  # [1,2]
# print(Solution.twoSum([2, 3, 4], 6))  # [1,3]
arr = ([-1] * 10000) + [1, 1]
print(Solution.twoSum(arr, 2))
