# The code below implements a very basic singly linked list.

class Node:
  def __init__(self, d):
    self.next = None
    self.data = d

  def append_to_tail(self, d):
    end = Node(d)
    n = self
    while n.next:
      n = n.next
    n.next = end 

  def delete_node(self, head, d):
    n = head

    if n.data == d:
      return head.next # moved head

    while n.next:
      if n.next.data == d:
        n.next = n.next.next
        return head # head didn't change
      n = n.next

    return head

  def print(self):
    n = self
    output = []
    while n:
      output.append(str(n.data))
      n = n.next
    print('->'.join(output)) 

# In this implementation, we don't have a LinkedList data structure. We access the linked list through a reference to the head Node of the linked list. When you implement the linked list this way, you need to be a bit careful. What is multiple objects need a reference to the linked list, and then the head of the linked list changes? Some objects might still be pointing to the old head.

# We could, if we chose, implement a LinkedList class that wraps the Node class. This would essentially just have a single member variable: the head Node. This would largely resolve the earlier issue.

# Remember that when you're discussing a linked list in an interview, you must understand whether it is a singly linked list or a doubly linked list.

class LinkedList:
  def __init__(self):
    self.head = None

# Deleting a node from a linked list is fairly straightforward. Given a node n, we find the previous node prev and set prev.next equal to n.next. If the list is doubly linked, we must also update n.next to set n.next.prev equal to n.prev. The important things to remember are (1) to check for the null pointer and (2) to update the head or tail pointer as necessary.

# Additionally, if you implement this code in C, C++ or another language that requires the developer to do memory management, you should consider if the removed node should be deallocated.

if __name__ == '__main__':
  n = Node(0)
  for i in range(1,5):
    n.append_to_tail(i)
  n.print()

  n.delete_node(n, 3)
  n.print()
