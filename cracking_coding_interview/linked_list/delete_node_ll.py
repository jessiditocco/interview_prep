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
        """Helpful representation of node object"""

        return "<head = {}, tail = {}>".format(self.head, self.tail)


    def delete_node(self, node):

        current = self.head

        while current.next is not None:
            # if we are deleting the first node
            if current.data == node.data and current == self.head:
                self.head == current.next

            # if we are deleting the last node
            elif current.data.next == node.data:
                current.next = current.next.next

            current = current.next

        # deleting the last node-- we must update the tail