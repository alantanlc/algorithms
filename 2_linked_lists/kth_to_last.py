# Question: Implement an algorithm to find the kth to last element of a singly linked list.

from linked_list import Node

def get_kth_to_last_element(head, k):
  # Description: Hint #126 - Can you do it iteratively? Imagine if you had two pointers pointing to adjacent nodes and they were moving at the same speed through the linked list. When one hits the end of the linked list, where will the other be?
  # Time: O(N)
  # Space: O(1)

  p1 = head
  p2 = head

  for i in range(k):
    if not p2.next:
      return
    p2 = p2.next

  while p2.next:
    p1 = p1.next
    p2 = p2.next

  return p1

if __name__ == '__main__':
  n = None
  for i in range(10):
    if not n:
      n = Node(i)
    else:
      n.append_to_tail(i)
  n.print()

  k = 3 
  print(get_kth_to_last_element(n, k).data)
