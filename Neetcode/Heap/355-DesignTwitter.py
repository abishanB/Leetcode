from typing import List
import heapq
from collections import Counter
from collections import deque


class Twitter:
  def __init__(self):
    self.count = 0
    self.tweets = dict()  # map user id to list of (count, tweetID)
    self.accounts_following = dict()  # map account id to set of following acc

  def postTweet(self, userId: int, tweetId: int) -> None:
    if userId not in self.tweets:
      self.tweets[userId] = []
    self.tweets[userId].append((-self.count, tweetId))
    self.count += 1

  def getNewsFeed(self, userId: int) -> List[int]:
    res = []
    heap = []

    if userId in self.accounts_following:  # add tweets from following users
      for followee in self.accounts_following[userId]:
        if followee in self.tweets:
          for tweet in self.tweets[followee]:
            heapq.heappush(heap, tweet)

    if userId in self.tweets:  # add users own tweets
      for tweet in self.tweets[userId]:
        heapq.heappush(heap, tweet)

    while heap and len(res) < 10:  # get 10 most recent
      tweet = heapq.heappop(heap)
      res.append(tweet[1])

    return res

  def follow(self, followerId: int, followeeId: int) -> None:
    if followeeId == followerId:
      return

    if followerId not in self.accounts_following:
      self.accounts_following[followerId] = set()

    self.accounts_following[followerId].add(followeeId)

  def unfollow(self, followerId: int, followeeId: int) -> None:
    if followeeId == followerId:
      return
    if followerId in self.accounts_following:
      self.accounts_following[followerId].discard(followeeId)


twitter = Twitter()
twitter.postTweet(1, 5)
n1 = twitter.getNewsFeed(1)
twitter.follow(1, 2)
twitter.postTweet(2, 6)
twitter.getNewsFeed(1)
twitter.unfollow(1, 2)
twitter.getNewsFeed(1)
