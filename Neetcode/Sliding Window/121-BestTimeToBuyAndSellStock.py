from typing import List


class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    l = 0
    r = 1
    res = 0

    while r < len(prices):
      if prices[l] < prices[r]:
        profit = prices[r] - prices[l]
        res = max(res, profit)
      else:
        l = r
      r += 1

    return res


Solution = Solution()
print(Solution.maxProfit([1, 2]))

# print(Solution.maxProfit([7, 1, 5, 3, 6, 4]))
# print(Solution.maxProfit([7, 6, 4, 3, 1]))
# print(Solution.maxProfit([1, 2, 4, 1, 5, 1, 6, 1, 3, 6, 7,
#                           1, 3, 6, 1, 5, 1, 5, 7, 8, 9, 2, 45, 2, 1, 24, 1, 12]))
