class Solution:
  def isPalindrome(self, s: str) -> bool:
    lowercaseStr = s.lower()

    pLeft = 0
    pRight = len(s) - 1

    while pLeft < pRight:
      if not lowercaseStr[pLeft].isalnum():  # ignore non alpha numeric chars
        pLeft += 1
        continue
      if not lowercaseStr[pRight].isalnum():
        pRight -= 1
        continue

      if lowercaseStr[pLeft] != lowercaseStr[pRight]:
        return False

      pLeft += 1
      pRight -= 1

    return True


Solution = Solution()
print(Solution.isPalindrome("0P"))
print(Solution.isPalindrome("a."))

# print(Solution.isPalindrome("A man, a plan, a canal: Panama".lower()))
# print(Solution.isPalindrome("race a car"))
# print(Solution.isPalindrome(" "))
