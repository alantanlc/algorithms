# Create Root Node: We create a Node class and assign a value to the node. This becomes a tree with only a root node.
class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  # The insert function compares the value of the node to the parent node
  # and decides to add it as a left node or a right node
  def insert(self, data):
    if self.data:
      if data < self.data:
        if self.left is None:
          self.left = Node(data) 
        else:
          self.left.insert(data)
      else:
        if self.right is None:
          self.right = Node(data)
        else:
          self.right.insert(data)
    else:
      self.data = data 

  # findval method to compare the value with nodes
  def findval(self, lkpval):
    if lkpval < self.data:
      if self.left is None:
        print(str(lkpval) + ' Not Found')
        return
      return self.left.findval(lkpval)
    elif lkpval > self.data:
      if self.right is None:
        print(str(lkpval) + ' Not Found')
        return
      return self.right.findval(lkpval)
    else:
      print(str(self.data) + ' Is Found')

  def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    print(self.data)
    if self.right:
      self.right.PrintTree()

# Create a root node
root = Node(12)
root.PrintTree()
print()

# Insert nodes
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
print()

# Find value in tree
root.findval(12)
root.findval(14)
root.findval(5)
root.findval(6)
root.findval(10)
root.findval(3)
