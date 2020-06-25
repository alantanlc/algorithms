# Question: Implement an algorithm to find the kth to last element of a singly linked list.

from linked_list import Node

def delete_middle_node(n):
  # Description: Update data of current node with data of next node and delete the next node. Assumption here is that input node is neither the first nor the last node of the singly linked list.
  # Time: O(1)
  # Space: O(1)

  n.data = n.next.data
  n.next = n.next.next

if __name__ == '__main__':
  head = Node(1)
  head.append_to_tail(5)
  head.append_to_tail(9)
  head.append_to_tail(12)
  head.print()

  n = head
  while n.data != 9:
    n = n.next
  print(n.data)

  delete_middle_node(n)

  head.print()

