from typing import List


class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:  # mySolutuion
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
      res[i] = prefix
      prefix *= nums[i]

    postfix = 1
    for j in range(len(nums) - 1, -1, -1):
      res[j] *= postfix
      postfix *= nums[j]

    return res


Solution = Solution()

print(Solution.productExceptSelf([1, 2, 3, 4]))
print(Solution.productExceptSelf([-1, 1, 0, -3, 3]))
