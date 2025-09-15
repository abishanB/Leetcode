class Solution(object):
  def canBeTypedWords(self, text, brokenLetters):
    words = text.split()
    broken = set(brokenLetters)

    res = len(words)  # assume all words can be typed
    for word in words:
      for char in word:
        if char in broken:
          res -= 1
          break

    return res
