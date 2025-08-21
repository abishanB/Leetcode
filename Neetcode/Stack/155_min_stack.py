from typing import List


class MinStack:

  def __init__(self):
    self.stack = []
    self.min = float('inf')

  def push(self, val: int) -> None:
    self.stack.append(val)
    if val < self.min:
      self.min = val

  def pop(self) -> None:
    val = self.stack.pop()
    if val == self.min:
      self.min = float('inf')
      for i in self.stack:
        if i < self.min:
          self.min = i

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.min
