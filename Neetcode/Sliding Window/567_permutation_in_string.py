class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    chars = dict()
    for c in s1:
      chars[c] = 1 + chars.get(c, 0)

    l = 0
    r = len(s1) - 1
    window = dict()
    for i in range(len(s1)):
      window[s2[i]] = 1 + window.get(s2[i], 0)
    if window == chars:
      return True
    l += 1
    r += 1
    while r < len(s2):
      window[s2[r]] = 1 + window.get(s2[r], 0)
      window[s2[l - 1]] -= 1
      if window[s2[l - 1]] == 0:
        window.pop(s2[l - 1])
      if window == chars:
        return True
      l += 1
      r += 1

    return False
