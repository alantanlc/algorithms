class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def getNumOfRects(points):
  answer = 0
  count = {}
  for p in points:
    for p_above in points:
      if p.x == p_above.x and p.y < p_above.y:
        pair = (p.y, p_above.y)
        if pair not in count:
          count[pair] = 0
        answer += count[pair]
        count[pair] += 1
  return answer

points = [Point(1,1), Point(2,1), Point(3,1), Point(1,2), Point(2,2), Point(3,2)]
print(getNumOfRects(points))
