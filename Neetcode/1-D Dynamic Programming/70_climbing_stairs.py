class Solution(object):
  def climbStairs(self, n):
    one, two = 1, 1
    for i in range(n - 1):
      prevOne = one
      one = one + two
      two = prevOne
    return one
