class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left:
        self.left.insert(value)
      else:
        self.left = Node(value)
    elif value > self.value:
      if self.right:
        self.right.insert(value)
      else:
        self.right = Node(value)

  def printTree(self):
    if self.value:
      if self.left:
        self.left.printTree()
      print(self.value)
      if self.right:
        self.right.printTree()

  def getDepth(self, depth=0):
    d = int(depth)
    if self.left:
      d += self.left.getDepth(depth+1)
    if self.right:
      d += self.right.getDepth(depth+1)
    return d

root = Node(2)
root.insert(1)
root.insert(3)

root.printTree()
print(root.getDepth())
