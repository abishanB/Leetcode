
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    s_dict = dict()
    t_dict = dict()

    # map how many times a char appears than compare the 2 maps
    for i in s:
      if i in s_dict:
        s_dict[i] += 1
      else:
        s_dict[i] = 1

    for i in t:
      if i in t_dict:
        t_dict[i] += 1
      else:
        t_dict[i] = 1

    return s_dict == t_dict


Solution = Solution()

print(Solution.isAnagram("anagram", "nagaram"))
print(Solution.isAnagram("car", "rat"))
