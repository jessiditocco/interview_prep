############################ using recursion ####################################
def n_factorial(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1

    return n_factorial(num - 1) * num

print n_factorial(0)
print n_factorial(1)
print n_factorial(2)
print n_factorial(3)
print n_factorial(5)

# We are doing straight recursion from n to n-1 all the way down to 1
# This will take O(n) time

############################ using iteration ####################################
def n_factorial(num):

    n_factorial = num
    mult_by = num - 1

    while mult_by > 0:
        n_factorial *= mult_by
        mult_by -=1

    return n_factorial

print n_factorial(0)
print n_factorial(1)
print n_factorial(2)
print n_factorial(3)
print n_factorial(5)
