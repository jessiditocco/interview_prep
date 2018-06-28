# class Queue(object):
#     def __init__(self):
#         self.data = []

#     def enqueue(self, item):
#         """Adds item to end of queue"""

#         self.data.append(item)

#     def dequeue(self):
#         """Pops item off of the front of the queue"""

#         if not self.data:
#             return None
#         else:
#             print "Okay, removing {}".format(self.data[0])
#             return self.data.pop(0)

#     def peak(self):
#         if not self.data:
#             return

#         return self.data[0]

#     def print_letters(self):
#         for item in self.data:
#             print item

#     def is_empty(self):
#         if not self.data:
#             return True


# class Stack(object):
#     def __init__(self):
#         self.data = []

#     def push(self, item):
#         """Pushes item on top of stack"""

#         self.data.append(item)

#     def pop(self):
#         """Pops item off of stack"""

#         if not self.data:
#             return None

#         else:
#             print "Okay, popping {} off the end of the stack".format(self.data[-1])
#             return self.data.pop()

#     def peak(self):

#         if not self.data:
#             return

#         return self.data[-1]


#     def print_letters(self):
#         for item in self.data:
#             print item


#     def is_empty(self):
#         if not self.data:
#             return True


# def is_palindrome(word):
#     """Determines if a word is a palindrome by using a stack and a queue"""

#     stack = Stack()
#     queue = Queue()

#     for letter in word:
#         stack.push(letter)
#         queue.enqueue(letter)

#     # import pdb; pdb.set_trace()

#     while not stack.is_empty() and not queue.is_empty():
#         if stack.pop() != queue.dequeue():
#             print "Not palindrome"
#             return False

#     print "Palindrome"
#     return True


############################# Hackerrank Solution ##############################
class Solution:
    # Write your code here
    def __init__(self):
        self._stack = []
        self._queue = []

    def print_stack(self):
        for i in self._stack:
            print i

    def print_queue(self):
        for i in self._queue:
            print i

    def pushCharacter(self, char):
        """Pushes charecter onto a stack"""

        self._stack.append(char)

    def enqueueCharacter(self, char):
        """Enqueues charecter onto queue"""

        self._queue.append(char)

    def popCharacter(self):
        """Pops character from stack"""

        return self._stack.pop()

    def dequeueCharacter(self):
        """Dequeues character from begining of queue"""

        return self._queue.pop(0)

# read the string s
s = raw_input()

#Create the Solution class object
obj = Solution()   

l = len(s)

# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

import pdb; pdb.set_trace();
isPalindrome = True
# # '''
# # pop the top character from stack
# # dequeue the first character from queue
# # compare both the characters
# # ''' 
for i in range(l / 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")    
    
        
