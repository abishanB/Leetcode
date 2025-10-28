class Solution:
  def romanToInt(self, s: str) -> int:
    sum = 0
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, "M": 1000}
    for i in range(len(s)):
      if (i + 1 < len(s)) and convert[s[i + 1]] > convert[s[i]]:
        sum -= convert[s[i]]
      else:
        sum += convert[s[i]]
    return sum


Solution = Solution()
print(Solution.romanToInt("MCMXCIV"))
