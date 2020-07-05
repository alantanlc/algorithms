# Question: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.

class LinkedListNode(object):
    
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def add(self, node):
        if node is None:
            return

        nxt = self
        while nxt.next is not None:
            nxt = nxt.next
        nxt.next = node

    def print(self):
        output = [str(self.data)]
        nxt = self.next
        while nxt is not None:
            output.append(f'->{nxt.data}')
            nxt = nxt.next
        print(''.join(output))


def partition(node: LinkedListNode, x: int) -> LinkedListNode:
    head = node
    tail = node

    while node is not None:
        nxt = node.next
        if node.data < x:
            # Insert node at head
            node.next = head
            head = node
        else:
            # Insert node at tail
            tail.next = node
            tail = node
        node = nxt
    tail.next = None

    # The head has changed, so we need to return it to the user
    return head


def main():
    head = LinkedListNode(3)
    head.add(LinkedListNode(5))
    head.add(LinkedListNode(8))
    head.add(LinkedListNode(5))
    head.add(LinkedListNode(10))
    head.add(LinkedListNode(2))
    head.add(LinkedListNode(1))
    head.print()

    rv = partition(head, 5)
    rv.print()


if __name__ == "__main__":
    main()
