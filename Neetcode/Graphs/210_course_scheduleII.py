from typing import List


class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

    preMap = {i: [] for i in range(numCourses)}
    for course, pre in prerequisites:
      preMap[course].append(pre)

    visited = set()
    res = []
    taken = set()

    def dfs(course):
      if course in visited:
        return []
      if preMap[course] == []:
        if course not in taken:
          res.append(course)
          taken.add(course)
        return True

      visited.add(course)
      for pre in preMap[course]:
        if not dfs(pre):
          return []

      visited.remove(course)
      preMap[course] = []
      if course not in taken:
        res.append(course)
        taken.add(course)
      return True

    for course in range(numCourses):
      if not dfs(course):
        return []
    return res
