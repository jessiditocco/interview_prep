class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

    def __repr__(self):
        return "<data={}, next={}>".format(self.data, self.next)

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "<head={}>".format(self.head)


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)

    if head is None:
        head = new_node
    else:
        head.next = new_node

    return head



if __name__ == "__main__":
    llist_count = int(raw_input())

    llist = SinglyLinkedList()

    for i in xrange(llist_count):
        llist_item = int(raw_input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head