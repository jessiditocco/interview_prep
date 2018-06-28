class Stack(object):
    """A stack class"""

    def __init__(self):
        self._stack = []


    def push(self, item):
        """Pushes item on top of stack"""

        self._stack.append(item)

    def pop(self):
        """Pops item from top of stack"""

        if self._stack:
            return self._stack.pop()

    def is_empty(self):
        """Returns true if stack is empty"""

        return not self._stack

    def peak(self):
        """Returns item at top of stack"""

        if not self.is_empty():
            return self._stack[-1]

        else:
            print "Stack is empty"
