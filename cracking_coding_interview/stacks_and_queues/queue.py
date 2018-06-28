class Queue(object):
    """A queue class"""

    def __init__(self):
        self._queue = []


    def enqueue(self, item):
        """Adds item to end of queue"""

        self._queue.append(item)

    def dequeue(self):
        """Removes item from begining of queue"""

        if not self.is_empty():
            return self._queue.pop(0)

        else:
            return "The queue is already empty"

    def is_empty(self):
        """Returns true if queue is empty"""

        return not self._queue

    def peak(self):
        """Returns item at the begining of the queue"""

        if not self.is_empty():
            return self._queue[0]

        else:
            print "Queue is empty"
