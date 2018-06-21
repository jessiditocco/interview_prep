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

    def length(self):
        count = 0

        if self.head is None:
            return count

        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def print_nodes(self):
        current = self.head

        while current:
            print current
            current = current.next

def move_pointer(ll, num_spots):
    current = ll.head

    for i in range(num_spots):
        current = current.next

    return current


def find_intersection(ll1, ll2):
    pointer_1 = None
    pointer_2 = None

    if ll1.tail != ll2.tail:
        return "No Intersection"

    if ll1.length() > ll2.length():
        num_spots = ll1.length() - ll2.length()
        pointer_1 = move_pointer(ll1, num_spots)
        pointer_2 = ll2.head
    elif ll2.length > ll1.length():
        print "ll2 longer"
        num_spots = ll2.length() - ll1.length()
        pointer_2 = move_pointer(ll2, num_spots)
        pointer_1 = ll1.head
    # else, Length of linked lists are equal
    else:
        pointer_1 = ll1.head
        pointer_2 = ll2.head

    # import pdb; pdb.set_trace();

    while pointer_1 is not None:
        if pointer_1 != pointer_2:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next

        elif pointer_1 == pointer_2:
            return pointer_1




if __name__ == "__main__":
    n1 = Node("3")
    n2 = Node("1")
    n3 = Node("5")
    n4 = Node("7")
    n5 = Node("2")
    n6 = Node("1")
    n7 = Node("4")
    n8 = Node("6")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    ll1 = LinkedList(n1, n6)

    n7.next = n8
    n8.next = n4
    n4.next = n5
    n5.next = n6

    ll2 = LinkedList(n7, n6)

    find_intersection(ll1, ll2)