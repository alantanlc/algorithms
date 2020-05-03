class Node:
  def __init__(self, dataval=None):
    self.dataval = dataval
    self.nextval = None

class SLinkedList:
  def __init__(self):
    self.headval = None

  def listprint(self):
    printval = self.headval
    while printval is not None:
      print(printval.dataval)
      printval = printval.nextval

  def AtBeginning(self, newdata):
    NewNode = Node(newdata)
    NewNode.nextval = self.headval
    self.headval = NewNode

  def InBetween(self, middle_node, newdata):
    if middle_node is None:
      print("The mentioned node is absent")
      return
    
    NewNode = Node(newdata)
    NewNode.nextval = middle_node.nextval
    middle_node.nextval = NewNode

  def AtEnd(self, newdata):
    NewNode = Node(newdata)
    if self.headval is None:
      self.headval = NewNode
      return
    EndNode = self.headval
    while EndNode.nextval:
      EndNode = EndNode.nextval
    EndNode.nextval = NewNode

  def RemoveNode(self, data):
    HeadNode = self.headval

    if HeadNode is not None and HeadNode.dataval == data:
      self.headval = HeadNode.nextval
      HeadNode = None
      return

    CurrentNode = HeadNode
    while CurrentNode.nextval:
      NextNode = CurrentNode.nextval
      if NextNode.dataval == data:
        CurrentNode.nextval = NextNode.nextval
        NextNode = None
        return  
      else:
        CurrentNode = CurrentNode.nextval

# Create Linked List
list = SLinkedList()

# Create nodes
e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Add first node to SLinkedList as head node
list.headval = e1

# Link first node to second node
e1.nextval = e2

# Link second node to third node
e2.nextval = e3

# Print SLinkedList
list.listprint()
print()

# Insert a new node at the beginning
list.AtBeginning("Sun")
list.listprint()
print()

# Insert a new node at the end
list.AtEnd("Fri")
list.listprint()
print()

# Insert a new node in the middle
list.InBetween(e3, "Thu")
list.listprint()
print()

# Delete a node by value
list.RemoveNode("Wed")
list.RemoveNode("Sun")
list.listprint()
