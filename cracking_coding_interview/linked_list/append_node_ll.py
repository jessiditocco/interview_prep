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

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        """Helpful representation of node object"""

        return "<head = {}, tail = {}>".format(self.head, self.tail)

    def append_node(self, data):
        """Appends a node with passed in data to a linked list"""

        # Append the node to the linked list
        # if its the only item, we must point head and tail to that item
        # if its not the first item, we must append it to the end and point the tail to it

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
