class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        """Helpful representation of node object"""

        return "<data = {}, next = {}>".format(self.data, self.next)


class LinkedList(object):
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __repr__(self):
        """Helpful representation of node object"""

        return "<head = {}, tail = {}>".format(self.head, self.tail)



def remove_dups(self):
    dup_counts = {}

    current = self.head

    while current.next is not None:
        dup_counts[current.data] = dup_counts.get(current.data, 0) + 1 

        if current.next.data in dup_counts:
            current.next = current.next.next

        else:
            current = current.next