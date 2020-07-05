# Question: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.


class Node(object):

    def __init__(self, data: int) -> None:
        self.next = None
        self.data = data

    def append_to_tail(self, d: int) -> None:
        end = Node(d)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end

    def print(self):
        output = [str(self.data)]
        n = self.next
        while n is not None:
            output.append(f'->{n.data}')
            n = n.next
        print(''.join(output))


def partition(node: Node, x: int) -> Node:
    before_start = None
    before_end = None
    after_start = None
    after_end = None

    # Partition list
    while node is not None:
        nxt = node.next
        node.next = None
        if node.data < x:
            # Insert node into end of before list
            if before_start is None:
                before_start = node
                before_end = before_start
            else:
                before_end.next = node
                before_end = node
        else:
            if after_start is None:
                after_start = node
                after_end = after_start
            else:
                after_end.next = node
                after_end = node
        node = nt

    if before_start is None:
        return after_start

    # Merge before list and after list
    before_end.next = after_start
    return before_start

def main():
    ll = Node(3)
    ll.append_to_tail(5)
    ll.append_to_tail(8)
    ll.append_to_tail(5)
    ll.append_to_tail(10)
    ll.append_to_tail(2)
    ll.append_to_tail(1)
    ll.print()

    result = partition(ll, 5)
    result.print()


if __name__ == '__main__':
    main()
