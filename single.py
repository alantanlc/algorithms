class Node:
  def __init__(self, value=0, next=None):
    self.value = value
    self.next = next

def addNode(value, head=None):
  temp = Node(value)
  if not head:
    head = temp
  else:
    p = head
    while p.next is not None:
      p = p.next
    p.next = temp
  return head

head = addNode(12)
addNode(99, head)
addNode(37, head)

print(head.next.value, head.next.next)

# delete node99
node99 = head.next
temp = node99.next
node99.value = temp.value
node99.next = temp.next
del temp

print(head.next.value, head.next.next)
