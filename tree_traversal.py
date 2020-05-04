
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def insert(self, data):
    if self.data:
      if data <= self.data:
        if not self.left:
          self.left = Node(data)
        else:
          self.left.insert(data)
      else:
        if not self.right:
          self.right = Node(data)
        else:
          self.right.insert(data)
    else:
      self.data = data

  def PrintTree(self):
    if self.data:
      if self.left:
        self.left.PrintTree()
      print(self.data)
      if self.right:
        self.right.PrintTree()

  def inorderTraversal(self, root):
    res = []
    if root:
      res = self.inorderTraversal(root.left)
      res.append(root.data)
      res = res + self.inorderTraversal(root.right)
    return res

  def preorderTraversal(self, root):
    res = []
    if root:
      res.append(root.data)
      res = res + self.preorderTraversal(root.left)
      res = res + self.preorderTraversal(root.right)
    return res

  def postorderTraversal(self, root):
    res = []
    if root:
      res = self.postorderTraversal(root.left)
      res = res + self.postorderTraversal(root.right)
      res.append(root.data)
    return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.PrintTree()    
print()

# In order traversal
print('In order traversal: ', root.inorderTraversal(root))

# Pre order traversal
print('Pre order traversal: ', root.preorderTraversal(root))

# Post order traversal
print('Post order traversal: ', root.postorderTraversal(root))
