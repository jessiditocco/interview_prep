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