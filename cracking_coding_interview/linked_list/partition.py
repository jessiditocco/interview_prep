# class Node(object):
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

#     def __repr__(self):
#         return "<data={}>".format(self.data, self.next)


# class LinkedList(object):
#     def __init__(self, head=None, tail=None):
#         self.head = head
#         self.tail = tail

#     def print_linked_list(self):
#         current = self.head

#         while current is not None:
#             print current.data
#             current = current.next

#     def __repr__(self):
#         return "<head={} tail={}>".format(self.head, self.tail)

#     def partition(self, partition):
#         # import pdb; pdb.set_trace();

#         smaller_than = LinkedList()
#         larger_than = LinkedList()

#         current = self.head

#         while current is not None:
#             new_node = Node(current.data)

#             if current.data < partition:
#                 if smaller_than.head is None:
#                     smaller_than.head = new_node
#                     smaller_than.tail = new_node
#                 else:
#                     smaller_than.tail.next = new_node
#                     smaller_than.tail = new_node

#             else:
#                 if larger_than.head is None:
#                     larger_than.head = new_node
#                     larger_than.tail = new_node
#                 else:
#                     larger_than.tail.next = new_node
#                     larger_than.tail = new_node
#             current = current.next

#         smaller_than.tail.next = larger_than.head

#         return smaller_than.print_linked_list()


# if __name__ == "__main__":
#     n1 = Node(4)
#     n2 = Node(5)
#     n3 = Node(9)
#     n4 = Node(1)
#     n5 = Node(3)
#     n1.next = n2
#     n2.next = n3
#     n3.next = n4
#     n4.next = n5

#     ll = LinkedList(n1, n5)

#     ll.partition(4)


#     n1 = Node(3)
#     n2 = Node(5)
#     n3 = Node(8)
#     n4 = Node(5)
#     n5 = Node(10)
#     n6 = Node(2)
#     n7 = Node(1)
#     n1.next = n2
#     n2.next = n3
#     n3.next = n4
#     n4.next = n5
#     n5.next = n6
#     n6.next = n7

#     ll = LinkedList(n1, n7)

#     ll.partition(7)


########### Another Implementation, passing only the head of the linkes list ############### 
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "<data={}>".format(self.data, self.next)


def partition_linked_list(head, pivot):
    a_head = None
    a_tail = None
    b_head = None
    b_tail = None

    current = head

    while current:
        if current.data < pivot:
            if a_head is None:
                a_head = current
                a_tail = current
            else:
                a_tail.next = current
                a_tail = current
        else:
            if b_head is None:
                b_head = current
                b_tail = current
            else:
                b_tail.next = current
                b_tail = current

        current = current.next

    a_tail.next = b_head

    return a_head


if __name__ == "__main__":
    n1 = Node(3)
    n2 = Node(5)
    n3 = Node(8)
    n4 = Node(5)
    n5 = Node(10)
    n6 = Node(2)
    n7 = Node(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7


