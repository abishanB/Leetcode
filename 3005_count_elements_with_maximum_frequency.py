from typing import List


class Solution:
  def maxFrequencyElements(self, nums: List[int]) -> int:

    freq = dict()
    maxFreq = 0
    maxFreqNums = []
    for n in nums:
      freq[n] = freq.get(n, 0) + 1
      if freq[n] > maxFreq:
        maxFreq = freq[n]
        maxFreqNums = [n]
      elif freq[n] == maxFreq:
        maxFreqNums.append(n)

    return maxFreq * len(maxFreqNums)
