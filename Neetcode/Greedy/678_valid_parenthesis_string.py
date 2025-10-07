class Solution:
  def checkValidString(self, s: str) -> bool:

    def dfs(open1, open2, open3, i):

      if open1 < 0 and open2 < 0 and open3 < 0:
        return False
      if i == len(s):
        if open1 == 0 or open2 == 0 or open3 == 0:
          return True
        return False
      if s[i] == "(":
        return dfs(open1 + 1, open2 + 1, open3 + 1, i + 1)
      if s[i] == ")":
        return dfs(open1 - 1, open2 - 1, open3 - 1, i + 1)

      return dfs(open1, open2 + 1, open3 - 1, i + 1)

    return dfs(0, 0, 0, 0)


Solution = Solution()
print(Solution.checkValidString("*)("))
