class Solution:
  def isHappy(self, n: int) -> bool:
    def sumOfSquares(n: int) -> int:
      output = 0

      while n:
        digit = n % 10
        digit = digit ** 2
        output += digit
        n = n // 10
      return output

    path = set()
    path.add(n)
    while n != 1:

      sumN = sumOfSquares(n)

      if sumN in path:
        return False
      path.add(sumN)
      n = sumN
    return True
