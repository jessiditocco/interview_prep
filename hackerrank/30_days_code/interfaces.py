# note  that interfaces are not necessary in Python becuaes Python has
# proper multiple inheritance, and also ducktyping, which means that places where
# you must have interfaces in Java, you dont have to have htem in python

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        number_sum = 0
        
        for i in range(1, n + 1):
            if (n % i) == 0:
                number_sum += i
                
        return number_sum


if __name__ == "__main__":
    n = int(raw_input())
    my_calculator = Calculator()
    s = my_calculator.divisorSum(n)
    print("I implemented: " + type(my_calculator).__bases__[0].__name__)
    print(s)