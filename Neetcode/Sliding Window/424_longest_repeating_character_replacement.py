class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    charCount = {}
    res = 0

    l = 0
    maxf = 0  # char with highest freq
    for r in range(len(s)):
      charCount[s[r]] = 1 + charCount.get(s[r], 0)
      maxf = max(maxf, charCount[s[r]])

      if (r - l + 1) - maxf > k:
        charCount[s[l]] -= 1
        l += 1

      res = max(res, r - l + 1)
    return res


Solution = Solution()
print(Solution.characterReplacement("ABABB", 2))
print(Solution.characterReplacement("AABABBA", 1))

print(Solution.characterReplacement("ABAB", 2))
