from typing import List


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
      mid = (l + r) // 2

      if nums[mid] == target:
        return True
      elif nums[mid] < target:
        l = mid + 1
      else:
        r = mid - 1

    return False

  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    l = 0
    r = len(matrix) - 1

    while l <= r:
      middle = (l + r) // 2
      if matrix[middle][0] <= target and matrix[middle][-1] >= target:
        return self.search(matrix[middle], target)

      elif matrix[middle][0] > target:
        r = middle - 1
      elif matrix[middle][-1] < target:
        l = middle + 1

    return False


Solution = Solution()
print(Solution.searchMatrix(
  [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
