from typing import List


class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    coins.sort()
    dp = [0] + [-1] * amount

    def calcMin(i):
      possible = []
      for c in coins:
        remaining = i - c
        if remaining < 0:
          continue
        if remaining == 0:
          return 1
        if dp[remaining] == -1:
          continue

        possible.append(dp[remaining] + 1)
      if not possible:
        return -1
      return min(possible)

    for i in range(1, amount + 1):
      dp[i] = calcMin(i)

    return dp[-1]
