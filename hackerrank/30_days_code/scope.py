class Difference(object):
    def __init__(self, a):
        self.arr = a

    def computeDifference(self):
        
        maxium = max(self.arr)
        minimum = min(self.arr)

        self.maximumDifference = abs(maxium - minimum)


if __name__ == "__main__":

    _ = raw_input()
    a = [int(e) for e in raw_input().split(' ')]

    d = Difference(a)

    d.computeDifference()

    print d.maximumDifference
