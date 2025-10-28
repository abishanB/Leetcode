from typing import List
from collections import Counter


class Solution:
  def removeAnagrams(self, words: List[str]) -> List[str]:  # my solution

    i = 0
    toRemove = []
    while i < len(words) - 1:
      if len(words[i]) != len(words[i + 1]):
        i += 1
        continue

      char_count = Counter(words[i])
      for j in range(i + 1, len(words)):
        if Counter(words[j]) == char_count:
          toRemove.append(j)
        else:
          break
      i = j

    for i in range(len(toRemove) - 1, -1, -1):
      words.pop(toRemove[i])
    return words


class Solution:  # optimal
  def removeAnagrams(self, words: List[str]) -> List[str]:
    res = [words[0]]
    for i in range(1, len(words)):

      if sorted(words[i]) != sorted(words[i - 1]):
        res.append(words[i])
    return res
