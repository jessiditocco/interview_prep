class SinglyLinkedListNode:
    def __init__(self, node_data, next=None):
        self.data = node_data
        self.next = next

    def __repr__(self):
        return "<data={}, next={}".format(self.data, self.next)


class SinglyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def printLinkedList(ll_head):

    while ll_head:
        print ll_head.data

        ll_head = ll_head.next


if __name__ == "__main__":
    llist_count = int(raw_input())

    llist = SinglyLinkedList()

    for _ in xrange(llist_count):
        llist_item = int(raw_input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)