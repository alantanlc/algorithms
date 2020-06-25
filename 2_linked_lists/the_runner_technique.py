from linked_list import Node

def get_start_pointers(head):
  p1 = head.next
  p2 = head

  while p1.next:
    p1 = p1.next.next
    p2 = p2.next

  return p1, p2.next

def weave(head):
  # p1 to move every 2 elements for every 1 move that p2 makes.
  # when p1 hits the end of the linked list, p2 will be at the endpoint.
  p1, p2 = get_start_pointers(head)

  # move p1 back to front and begin "weaving" the elements
  p1 = head

  output = []
  while p2:
    output.append(str(p1.data))
    output.append(str(p2.data))
    p1 = p1.next
    p2 = p2.next
  print('->'.join(output))


if __name__ == '__main__':
  n = Node(0)
  for i in range(1, 6):
    n.append_to_tail(i)
  n.print()
  weave(n)
