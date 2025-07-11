
class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0:  # negatives are not palindrome
      return False
    if x < 10:  # single digit is palindrome
      return True

    n = x
    e = 0  # how big the number is in regards to 10^e
    while n >= 10:  # divide by 10 till only the one digit is before the decimal
      e += 1
      n /= 10

    num = x
    for i in range(0, e, 2):
      first = num // 10**(e - i)
      last = num % 10
      if first == last:
        num = (num % (10 ** (e - i))) // 10
      else:
        return False
    return True


Solution = Solution()
print(Solution.isPalindrome(10021))
