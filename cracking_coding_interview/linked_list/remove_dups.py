class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        """Helpful representation of node object"""

        return "<data = {}, next = {}>".format(self.data, self.next)


class LinkedList(object):
    def __init__(self, head, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        """Helpful representation of node object"""

        return "<head = {}, tail = {}>".format(self.head, self.tail)



    def remove_dups(self):
        # import pdb; pdb.set_trace()

        if ll.head is None:
            return

        dups = set()

        current = self.head

        while current.next is not None:
            dups.add(current.data)

            if current.next.data in dups:
                current.next = current.next.next
                
                if current.next is None:
                    self.tail = current

            else:
                current = current.next


if __name__ == "__main__":
    n1 = Node("apple")
    n2 = Node("berry")
    n3 = Node("cherry")
    n4 = Node("berry")
    n5 = Node("apple")
    n6 = Node("apple")
    n7 = Node("berry")
    n8 = Node("durian")
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8

    ll = LinkedList(n1, n8)

    # ll.remove_dups()