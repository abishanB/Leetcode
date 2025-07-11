from typing import List


class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 1:
      return strs[0]

    shortestStr = len(strs[0])
    shortestWord = strs[0]
    for i in range(len(strs)):
      if len(strs[i]) < shortestStr:
        shortestStr = len(strs[i])
        shortestWord = strs[i]

    if shortestStr == 0:
      return ""

    prefix = shortestWord[0]
    for j in range(1, shortestStr + 1):
      prefix = shortestWord[:j]
      for k in range(len(strs)):
        if strs[k].startswith(prefix):
          continue
        return prefix[:-1]

    return prefix


Solution = Solution()
print(Solution.longestCommonPrefix(["flower", "flow", "flight"]))
#
# print(Solution.longestCommonPrefix(["dog", "racecar", "car"]))
print(Solution.longestCommonPrefix(["flower", "flower", "flower", "flower"]))
