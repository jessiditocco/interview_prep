def calculate_fibonacci(n):
    """Returns the nth fibonacci sequence, given a number n"""

    if n == 0:
        return 0
    elif n == 1: 
        return 1

    return calculate_fibonacci(n - 2) + calculate_fibonacci(n - 1)



print calculate_fibonacci(1)
print calculate_fibonacci(2)
print calculate_fibonacci(3)
print calculate_fibonacci(4)
print calculate_fibonacci(5)
print calculate_fibonacci(6)
print calculate_fibonacci(7)

# Runtime is O(branches ^ depth)
# O(2^n) --> exponential