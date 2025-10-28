class Solution:
  def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:  # my solution
    exchangeMap = dict()

    def dfs(numBottles, exchange, empty, drunk):
      if (numBottles, exchange, empty) in exchangeMap:
        d = exchangeMap[(numBottles, exchange, empty)]
        return d

      if numBottles == 0 and empty < exchange:
        return drunk

      drinkOption = 0
      exchangeOption = 0
      if numBottles != 0:
        drinkOption = dfs(0, exchange, empty + numBottles, drunk + numBottles)

      if empty >= exchange:
        exchangeOption = dfs(numBottles + 1, exchange +
                             1, empty - exchange, drunk)
      exchangeMap[(numBottles, exchange, empty)] = max(
        drinkOption, exchangeOption)
      return max(drinkOption, exchangeOption)

    return dfs(numBottles, numExchange, 0, 0)

  def maxBottlesDrunk1(self, numBottles: int, numExchange: int) -> int:  # Greedy Approach
    drunk = numBottles
    empty = numBottles

    while empty >= numExchange:
      empty -= numExchange
      numExchange += 1
      drunk += 1
      empty += 1
    return drunk
