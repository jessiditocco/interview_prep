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


    def delete_node(self, value):

        # if your removing the head, we need to 
        # point the second item to the new head

        if self.head.data == value:
            self.head = self.head.next


        # removing something other than the head
        # current is equal to the head

        current = self.head

        # while the current's next is not none
        # check if current's next's data is equal to the value
        # if it is, set current's next equal to its next next
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next

                # if you're removing the last item and the current.next is None
                # update the tail

                if current.next is None:
                    self.tail = current
                return
            # havent found the value yet, keep traversing
            else:
                current = current.next

