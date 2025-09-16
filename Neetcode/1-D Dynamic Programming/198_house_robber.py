class Solution(object):
  def rob(self, nums):
    if len(nums) == 1:
      return nums[0]

    for i in range(len(nums) - 2, -1, -1):
      if i == len(nums) - 2:
        continue
      if i == len(nums) - 3:
        nums[i] = nums[i] + nums[-1]
        continue
      nums[i] = max(nums[i + 2] + nums[i], nums[i + 3] + nums[i])

    return max(nums[0], nums[1])
