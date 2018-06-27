class Node(object):
    """A linked list node class"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # def __repr__(self):
        # return "<data={} next={}>".format(self.data, self.next)

class LinkedList(object):
    """A linked list class"""

    def __init__(self, head, tail=None):
        self.head = head
        self.tail = tail

    # def __repr__(self):
        # return "<head={} tail={}>".format(self.head, self.tail)

    def print_nodes(self):
        current = self.head

        while current:
            print current.data
            current = current.next


def loop_detection(ll):
    """Returns the node at the beggining of the loop"""

    current = ll.head

    seen = set()

    while current:
        if current not in seen:
            seen.add(current)
            current = current.next
        else:
            print current.data
            break


if __name__ == "__main__":
    n1 = Node("A")
    n2 = Node("B")
    n3 = Node("C")
    n4 = Node("D")
    n5 = Node("E")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n3

    ll = LinkedList(n1)