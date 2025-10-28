class Solution:
  def totalMoney(self, n: int) -> int:
    weeks = n // 7
    daysLeft = n - (weeks * 7)
    res = 0
    for w in range(1, weeks + 1):
      res += 7 * (w + 3)
    for i in range(1, daysLeft + 1):
      res += (weeks) + i
    return res


class Solution:
  def totalMoney(self, n: int) -> int:
    weeks = n // 7
    daysLeft = n - (weeks * 7)
    end = 4 + weeks - 1
    # sum from weeks == 7 * (4+5+6...)
    sumWeeks = ((end - 4 + 1) * (4 + end)) // 2
    res = 0
    if weeks != 0:
      res = sumWeeks * 7
    for i in range(1, daysLeft + 1):
      res += (weeks) + i
    return res
