class Solution:
  def isValid(self, s: str) -> bool:
    curlyBrackets = 0
    squareBrackets = 0
    circleBrackets = 0
    for i in range(len(s)):
      if s[i] == "{":
        curlyBrackets += 1
      elif s[i] == "[":
        squareBrackets += 1
      elif s[i] == "(":
        circleBrackets += 1
      elif s[i] == "}":
        curlyBrackets -= 1
      elif s[i] == "]":
        squareBrackets -= 1
      elif s[i] == ")":
        circleBrackets -= 1

    if curlyBrackets == 0 and squareBrackets == 0 and circleBrackets == 0:
      return True
    return False


Solution = Solution()
print(Solution.isValid("[{}]"))
print(Solution.isValid("()[]{}"))
print(Solution.isValid("(]"))
