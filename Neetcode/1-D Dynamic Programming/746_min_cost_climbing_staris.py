class Solution(object):
  def minCostClimbingStairs(self, cost):
    dp = [-1] * len(cost)
    two = cost[-1]
    one = cost[-2]
    for i in range(len(cost) - 3, -1, -1):
      temp = one
      one = cost[i] + min(one, two)
      two = temp
    return min(one, two)
