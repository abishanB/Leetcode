class Solution:
  def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    def dfs(numBottles, empty, total):
      if numBottles == 0:
        return total

      empty += numBottles
      exchange = (empty) // numExchange
      empty = (empty) % numExchange

      return dfs(exchange, empty, total + numBottles)

    return dfs(numBottles, 0, 0)
