class Node(object):
    """A node class for a linked list"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    def __repr__(self):
        """Helpful representation of node object"""

        return "<data = {}, next = {}>".format(self.data, self.next)


class LinkedList(object):
    """A linked list class"""

    def __init__(self, head, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        """Helpful representation of Linked list object"""

        return "<head = {}, tail = {}>".format(self.head, self.tail)

