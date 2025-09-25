class TimeMap:
  def __init__(self):
    self.map = dict()

  def set(self, key: str, value: str, timestamp: int) -> None:
    if key not in self.map:
      self.map[key] = [(timestamp, value)]
    else:
      self.map[key].append((timestamp, value))

  def get(self, key: str, timestamp: int) -> str:
    if key not in self.map:
      return ""

    arr = self.map[key]
    l, r = 0, len(arr) - 1
    res = ""

    while l <= r:
      mid = (l + r) // 2
      t, v = arr[mid]

      if t == timestamp:
        return v
      elif t < timestamp:
        res = v
        l = mid + 1
      else:
        r = mid - 1
    return res
