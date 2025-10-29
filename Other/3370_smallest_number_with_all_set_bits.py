class Solution:
  def smallestNumber(self, n: int) -> int:
    x = 1
    step = 1
    while x < n:
      x += 2 ** step
      step += 1
    return x
