# Question: Write code to remove duplicates from an unsorted linked list.

from linked_list import Node

def remove_dup_1(head):
  # Description: Use a hash table. You should be able to do this in a single pass of the linked list.
  # Time: O(N)
  # Space: O(N)
  seen = {}
  n = head
  while n.next:
    if n.next.data not in seen:
      seen[n.next.data] = True
      n = n.next
    else:
      n.next = n.next.next
  return head

def remove_dup_2(head):
  # Description: Without extra space, you'll need O(N^2) time. Try using two pointers, where the second one searches ahead of the first one.
  # Time: O(N^2)
  # Space: O(1)
  p1 = head
  while p1:
    p2 = p1
    while p2.next:
      if p2.next.data == p1.data:
        p2.next = p2.next.next
      else:
        p2 = p2.next
    p1 = p1.next
  return head

if __name__ == '__main__':
  n = None
  for i in range(6):
    if not n:
      n = Node(i)
    else:
      n.append_to_tail(i)
  n.append_to_tail(5)
  n.print()
  n = remove_dup_2(n)
  n.print()
