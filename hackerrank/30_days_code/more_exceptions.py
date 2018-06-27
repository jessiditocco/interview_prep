class Calculator(object):

     # 3 ^ 3 = 3 * 3 * 3
    def power(self, n, p):
        if n <= 0 or p < 0:
            raise ValueError("Should be positive")
        if p == 0:
            return 1
        elif p == 1:
            return n

        return n * self.power(n, p-1)



if __name__ == "__main__":

    myCalculator = Calculator()
    num_cases = int(raw_input())

    for i in range(num_cases):
        n,p = map(int, raw_input().split())

        try:
            ans = myCalculator.power(n,p)
            print ans
        except Exception, e:
            print e