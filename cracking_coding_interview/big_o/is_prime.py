from math import sqrt

def is_prime(num):
    # if number is 0, 1-- > return False bc 0 and 1 are not prime
    # A number is prime if its divisible by only 1 and itself
    # we want to loop through numbers in the range of 2 to the square root
    # of the number to determine whether its pirime
    # we will check the modulo of num / i and if its equal to zero, we will
    # return False
    # return True at end

    if num < 2:
        return False

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

    # This runs on O(sqrt(n)) time becuase the work inside of the for
    # loop is constant
    # we just need to know how many iterations the for loop goes
    # through in worst case-- which is from 2 to the squareroot of n


print is_prime(1)
print is_prime(2)
print is_prime(3)
print is_prime(4)
print is_prime(5)
print is_prime(6)
print is_prime(7)
print is_prime(11)
