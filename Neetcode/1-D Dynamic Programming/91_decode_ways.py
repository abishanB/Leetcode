class Solution(object):
  def numDecodings1(self, s):  # neetcode solutions
    dp = {len(s): 1}

    def dfs(i):
      if i in dp:
        return dp[i]
      if s[i] == "0":
        return 0

      res = dfs(i + 1)
      if i + 1 < len(s) and (
          s[i] == "1" or s[i] == "2" and
          s[i + 1] in "0123456"
      ):
        res += dfs(i + 2)
      dp[i] = res
      return res

    return dfs(0)

  def numDecodings(self, s):  # my solution

    res = 0
    decodeMap = dict()
    nums = set("0123456")

    def dfs(s):
      if s == "":
        return 1

      if s in decodeMap:
        return decodeMap[s]

      if s[0] == "0":
        return 0

      res = 0
      res += dfs(s[1:])

      if len(s) > 1:
        if s[0] == "1" or s[0] == "2" and s[1] in nums:
          res += dfs(s[2:])

      decodeMap[s] = res
      return res

    res += dfs(s)
    return res
