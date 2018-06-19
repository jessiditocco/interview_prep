# Python comes with a module which provides infrastructure for
# defining Abstract Base Classes (ABCs)

from abc import ABCMeta, abstractmethod

class Book:
    __metaclass__ = ABCMeta
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display():
        pass

    
class MyBook(Book):
    def __init__(self, title, author, price):
        super(MyBook, self).__init__(title, author)
        self.price = price

    def display(self):
        print "Title: {}".format(self.title)
        print "Author: {}".format(self.author)
        print "Price: {}".format(str(price))

if __name__ == "__main__":
    title = input()
    author = input()
    price = int(input())

# A class that is derived from an abstract class cannot be 
# Instantiated unless all of its abstract methods are overriden