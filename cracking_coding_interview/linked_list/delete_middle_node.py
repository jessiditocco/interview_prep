class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "<data {} next {}>".format(self.data, self.next)


class LinkedList(object):
    def __init__(self, head, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        return "<head {} tail {}>".format(self.head, self.tail)

    def delete_middle_node(self, node):
        if node is None or node.next == None:
            return "You cannot delete the last node/ node must be valid"
        elif node == self.head:
            return "You cannot delete the head"

        next = node.next

        node.data = next.data
        node.next = next.next

        return self


if __name__ == '__main__':
    n1 = Node("a")
    n2 = Node("b")
    n3 = Node("c")
    n4 = Node("d")

    n1.next = n2
    n2.next = n3
    n3.next = n4

    ll = LinkedList(n1)