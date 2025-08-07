from typing import List


class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    for row in board:  # rows
      rowNoBlankSpaces = [elem for elem in row if elem != '.']

      if (len(rowNoBlankSpaces) != len(set(rowNoBlankSpaces))):
        return False

    for col in range(9):  # cols
      colNums = set()
      for row in range(9):
        if board[row][col] == ".":
          continue
        if board[row][col] in colNums:
          return False
        colNums.add(board[row][col])

    for row in range(0, 9, 3):  # boxes
      for col in range(0, 9, 3):
        subBoxNums = set()
        for i in range(3):
          for j in range(3):
            if board[row + i][col + j] == ".":
              continue
            if board[row + i][col + j] in subBoxNums:
              return False
            subBoxNums.add(board[row + i][col + j])

    return True


Solution = Solution()

# print(Solution.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
#       "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
# print(Solution.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
#     "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(Solution.isValidSudoku([[".", ".", "4", ".", ".", ".", "6", "3", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], ["5", ".", ".", ".", ".", ".", ".", "9", "."], [".", ".", ".", "5", "6", ".", ".", ".", "."], [
      "4", ".", "3", ".", ".", ".", ".", ".", "1"], [".", ".", ".", "7", ".", ".", ".", ".", "."], [".", ".", ".", "5", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."]]))
