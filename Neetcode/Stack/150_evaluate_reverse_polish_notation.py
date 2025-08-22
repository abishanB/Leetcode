from typing import List


class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    stack = []

    for t in tokens:
      if t == "+":
        res = stack.pop() + stack.pop()
        stack.append(res)
      elif t == "*":
        res = stack.pop() * stack.pop()
        stack.append(res)
      elif t == "-":
        res = stack[-2] - stack[-1]
        stack.pop()
        stack.pop()
        stack.append(res)
      elif t == "/":
        res = int(stack[-2] / stack[-1])
        stack.pop()
        stack.pop()
        stack.append(res)
      else:
        stack.append(int(t))

    return stack[0]
