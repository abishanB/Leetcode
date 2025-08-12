from typing import List


class Solution:
  def encode(self, strs: List[str]) -> str:
    res = ""
    for s in strs:
      res += str(len(s)) + "#" + s
    return res

  def decode(self, s: str) -> List[str]:
    res = []
    i = 0
    while len(s) > 2:
      j = i
      while s[j] != "#":
        j += 1

      length = int(s[i:j])

      res.append(s[j + 1: j + length + 1])
      s = s[i + length + 1:]
      i = j + + length
    return res


Solution = Solution()
print(Solution.encode(['ri6ver', 'sto5ne', 'l1eaf',
      'clo4ud', 'fla0me', 'shad7ow', 'wi2nd', 'bre1eze']))

print(Solution.decode("6#ri6ver6#sto5ne5#l1eaf6#clo4ud6#fla0me7#shad7ow5#wi2nd7#bre1eze"))
