from typing import List


class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    l, r = 0, 0

    words = set(wordDict)
    while l <= r and r < len(s):
      c = s[l:r + 1]
      if c in words:
        if r == len(s) - 1:
          return True

        l = r + 1

      r += 1
    return False


Solution = Solution()
# print(Solution.wordBreak("leetcode", ["leet", "code"]))
print(Solution.wordBreak("aaaaaaa", ["aaaa", "aaa"]))
