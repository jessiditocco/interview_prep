
########################## Reverse and Compare ################################


# class Node(object):
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

#     def __repr__(self):
#         return "<data={} next={}>".format(self.data, self.next)


# class LinkedList(object):
#     def __init__(self, head=None, tail=None):
#         self.head = head
#         self.tail = tail

#     def __repr__(self):
#         return "<head={} tail={}>".format(self.head, self.tail)

#     def print_nodes(self):
#         current = self.head

#         while current:
#             print current.data
#             current = current.next


# def copy_and_reverse_ll(head):
#     prev = None
#     current = copy(head)

#     while current:
#         next = current.next
#         current.next = prev
#         prev = current
#         current = copy(next)

#     return prev


# def copy(node):
#     if node:
#         return Node(node.data, node.next)

#     else:
#         return None


# def is_palindrome(ll):
#     # import pdb; pdb.set_trace()

#     # make a copy of the linked list-- reversed
    
#     reversed_copy = copy_and_reverse_ll(ll.head)

#     # loop through the original linked list and check that all of the letters are equal

#     current = ll.head

#     while current:
#         if current.data != reversed_copy.data:
#             return False

#         current = current.next
#         reversed_copy = reversed_copy.next

#     return True


########################## Iterative Approach ################################
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


def is_palindrome(ll):
    # import pdb; pdb.set_trace()

    fast = ll.head
    slow = ll.head

    letter_stack = []

    while fast and fast.next:
        letter_stack.append(slow.data)

        slow = slow.next
        fast = fast.next.next

    # if we have an odd number of nodes, we want to discount that middle node
    # and start on the next node
    if fast:
        slow = slow.next

    while slow:
        top = letter_stack.pop()
        if slow.data != top:
            return False

        slow = slow.next

    return True




if __name__ == "__main__":
    n1 = Node("t")
    n2 = Node("a")
    n3 = Node("c")
    n4 = Node("o")
    n5 = Node("c")
    n6 = Node("a")
    n7 = Node("t")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    ll9 = LinkedList(n1, n7)

    is_palindrome(ll9)

    n1 = Node("a")
    n2 = Node("b")
    n3 = Node("c")
    n4 = Node("d")

    n1.next = n2
    n2.next = n3
    n3.next = n4

    ll10 = LinkedList(n1, n4)

    n1 = Node("c")
    n2 = Node("a")
    n3 = Node("r")
    n4 = Node("r")
    n5 = Node("a")
    n6 = Node("c")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    ll11 = LinkedList(n1, n6)

