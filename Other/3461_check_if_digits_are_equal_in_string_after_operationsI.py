class Solution:
  def hasSameDigits(self, s: str) -> bool:
    digits = list(s)
    n = len(digits)
    for i in range(n):
      digit = int(digits[i])
      digits[i] = digit

    res = []
    while len(digits) > 2:
      for i in range(len(digits) - 1):
        mod = (digits[i] + digits[i + 1]) % 10
        res.append(mod)
      digits = res
      res = []

    return digits[0] == digits[1]
