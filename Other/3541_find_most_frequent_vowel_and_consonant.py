class Solution(object):
  def maxFreqSum(self, s):
    vowels = set("aeiou")
    consonants = set("qwrtypsdfghjklzxcvbnm")

    vowelMap = dict()
    consonantMap = dict()
    vowelMax = 0
    consonantMax = 0
    for c in s:
      if c in vowels:
        vowelMap[c] = vowelMap.get(c, 0) + 1
      if c in consonants:
        consonantMap[c] = consonantMap.get(c, 0) + 1
      vowelMax = max(vowelMax, vowelMap[c])
      consonantMax = max(consonantMax, consonantMap[c])
    return vowelMax + consonantMax
