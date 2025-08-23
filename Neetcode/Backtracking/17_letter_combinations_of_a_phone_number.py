from typing import List


class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    res = []
    num_to_letters = {
      '2': ["a", "b", "c"],
      '3': ["d", "e", "f"],
      '4': ["g", "h", "i"],
      '5': ["j", "k", "l"],
      '6': ["m", "n", "o"],
      '7': ["p", "q", "r", "s"],
      '8': ["t", "u", "v"],
      '9': ["w", "x", "y", "z"]
    }

    def backtrack(digits_str, word):
      for n in range(len(digits_str)):
        for l in num_to_letters[digits_str[n]]:
          word += l
          if len(word) == len(digits):
            res.append(word)
          backtrack(digits_str[n + 1:], word)
          word = word[:-1]
    backtrack(digits, "")
    return res
