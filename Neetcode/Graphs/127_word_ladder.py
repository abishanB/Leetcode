from typing import List
from collections import deque
import collections


class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
      return 0

    # maps neigboruing words, {h*t: [hot, hit]}
    nei = collections.defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
      for j in range(len(word)):
        pattern = word[:j] + "*" + word[j + 1:]
        nei[pattern].append(word)

    visit = set([beginWord])
    q = deque([beginWord])
    res = 1

    while q:
      for i in range(len(q)):
        word = q.popleft()
        if word == endWord:
          return res

        for j in range(len(word)):
          pattern = word[:j] + "*" + word[j + 1:]
          for neighbour in nei[pattern]:
            if neighbour not in visit:
              visit.add(neighbour)
              q.append(neighbour)

      res += 1
    return 0
