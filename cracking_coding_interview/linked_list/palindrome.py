class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "<data={} next={}>".format(self.data, self.next)


class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        return "<head={} tail={}>".format(self.head, self.tail)

    def print_nodes(self):
        current = self.head

        while current:
            print current.data
            current = current.next


def copy_and_reverse_ll(head):
    prev = None
    current = copy(head)

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = copy(next)

    return prev


def copy(node):
    if node:
        return Node(node.data, node.next)

    else:
        return None


def is_palindrome(ll):
    # import pdb; pdb.set_trace()

    # make a copy of the linked list-- reversed
    
    reversed_copy = copy_and_reverse_ll(ll.head)

    # loop through the original linked list and check that all of the letters are equal

    current = ll.head

    while current:
        if current.data != reversed_copy.data:
            return False

        current = current.next
        reversed_copy = reversed_copy.next

    return True

# def is_palindrome_optimized(ll):

#     # we only need to loop through the first half of the linked list
#     # to compare the the reversed linked list copy

#     reversed_copy = copy_and_reverse_ll(ll.head)

#     # loop through the original linked list and check that all of the letters are equal

#     current = ll.head

#     while current:
#         if current.data != reversed_copy.data:
#             return False

#         current = current.next
#         reversed_copy = reversed_copy.next

#     return True





if __name__ == "__main__":
    n1 = Node("t")
    n2 = Node("a")
    n3 = Node("c")
    n4 = Node("o")
    n5 = Node("b")
    n6 = Node("e")
    n7 = Node("l")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    ll14 = LinkedList(n1, n7)

    is_palindrome(ll14)
