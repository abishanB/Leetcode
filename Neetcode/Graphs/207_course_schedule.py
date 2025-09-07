from typing import List


class Solution:
  def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # optimal solution
    preMap = {i: [] for i in range(numCourses)}
    for course, pre in prerequisites:
      preMap[course].append(pre)

    visited = set()

    def dfs(course):
      if course in visited:
        return False
      if preMap(course) == []:
        return True

      visited.add(course)
      for pre in preMap[course]:
        if not dfs(pre):
          return False

      visited.remove(course)
      preMap[course] = []
      return True

    for course in range(numCourses):
      if not dfs(course):
        return False
    return True

  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # my solution
    courses = dict()

    for i in range(numCourses):
      courses[i] = set()

    for [course, pre] in prerequisites:
      courses[course].add(pre)

    taken = set()
    for course in courses:
      if courses[course] == []:
        taken.add(course)

    while len(taken) != numCourses:
      update = False
      for course in courses:
        if courses[course].issubset(taken) and course not in taken:

          taken.add(course)
          update = True

      if not update:
        return False

    return True


Solution = Solution()
print(Solution.canFinish(3, [[1, 0], [1, 2], [0, 1]]))
