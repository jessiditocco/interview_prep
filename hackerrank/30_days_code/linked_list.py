class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution(object):
    
    def display(self, head):
        current = head
        while current:
            print current.data

            current = current.next

    def insert(self, head, data):
        new_node = Node(data)

        if head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        return self.head



if __name__ == "__main__":
    mylist = Solution()
    head = None

    T = int(input())

    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)

    mylist.display(head)
