class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "<Node: data {} next {}>".format(self.data, self.next)

class LinkedList(object):
    def __init__(self, head, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        return "<LL Head {} LL tail {}>".format(self.head, self.tail)


    def kth_to_last(self, k):
        # import pdb; pdb.set_trace()
        runner = self.head
        current = self.head

        for i in range(k):
            if runner is None:
                return None
            runner = runner.next
        
        while runner:
            current = current.next
            runner = runner.next

        return current

    def kth_to_last_recursive(self, current, k):
        


if __name__ == "__main__":
    n1 = Node("apple")
    n2 = Node("berry")
    n3 = Node("cherry")
    n4 = Node("berry")
    n1.next = n2
    n2.next = n3
    n3.next = n4

    ll = LinkedList(n1, n4)