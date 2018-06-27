class Queue(object):
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        """Adds item to end of queue"""

        self.data.append(item)

    def dequeue(self):
        """Pops item off of the front of the queue"""

        if not self.data:
            return None
        else:
            print "Okay, removing {}".format(self.data[0])
            return self.data.pop(0)

    def peak(self):
        if not self.data:
            return

        return self.data[0]

    def print_letters(self):
        for item in self.data:
            print item

    def is_empty(self):
        if not self.data:
            return True


class Stack(object):
    def __init__(self):
        self.data = []

    def push(self, item):
        """Pushes item on top of stack"""

        self.data.append(item)

    def pop(self):
        """Pops item off of stack"""

        if not self.data:
            return None

        else:
            print "Okay, popping {} off the end of the stack".format(self.data[-1])
            return self.data.pop()

    def peak(self):

        if not self.data:
            return

        return self.data[-1]


    def print_letters(self):
        for item in self.data:
            print item


    def is_empty(self):
        if not self.data:
            return True


def is_palindrome(word):
    """Determines if a word is a palindrome by using a stack and a queue"""

    stack = Stack()
    queue = Queue()

    for letter in word:
        stack.push(letter)
        queue.enqueue(letter)

    # import pdb; pdb.set_trace()

    while not stack.is_empty() and not queue.is_empty():
        if stack.pop() != queue.dequeue():
            print "Not palindrome"
            return False

    print "Palindrome"
    return True

