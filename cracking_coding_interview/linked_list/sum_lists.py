class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "<data={}>".format(self.data)


class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        return "<head={} tail={}>".format(self.head, self.tail)


    def print_ll(self):
        current = self.head

        while current is not None:
            print current

            current = current.next

    def add(self, data):
        new_node = Node(data)
        current = self.head

        if not current:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

# def sum_linked_lists(num1, num2):

        
#     num1_digits = []
#     num2_digits = []
#     sum_nums = LinkedList()

#     current = num1.head

#     while current:
#         num1_digits.append(current.data)

#         current = current.next

#     current = num2.head

#     while current:
#         num2_digits.append(current.data)

#         current = current.next

#     num1_digits.reverse()
#     num2_digits.reverse()

#     num_1 = int("".join(map(str, num1_digits)))
#     num_2 = int("".join(map(str, num2_digits)))


#     str_sum_nums = reversed(str(num_1 + num_2))


#     for digit in str_sum_nums:
#         new_node = Node(digit)

#         if sum_nums.head is None:
#             sum_nums.head = new_node
#             sum_nums.tail = new_node

#         else:
#             sum_nums.tail.next = new_node
#             sum_nums.tail = new_node

#     return sum_nums.print_ll()

def sum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head

    ll = LinkedList()
    carry = 0

    while n1 or n2:
        result = carry

        if n1:
            result += n1.data
            n1 = n1.next

        if n2:
            result += n2.data
            n2 = n2.next

        ll.add(result % 10)
        carry = result // 10

    if carry:
        ll.add(carry)

    return ll.print_ll()



if __name__ == '__main__':
    n1 = Node(7)
    n2 = Node(1)
    n3 = Node(6)

    n4 = Node(5)
    n5 = Node(9)
    n6 = Node(2)

    n1.next = n2
    n2.next = n3
 

    n4.next = n5
    n5.next = n6

    linked_list1 = LinkedList(n1)
    linked_list2 = LinkedList(n4)

