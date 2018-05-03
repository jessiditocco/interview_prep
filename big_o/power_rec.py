def power(a, b):
    """Implements function that calculates a raised to the power of b"""

    if b == 0:
        return 1

    return a * power(a, (b - 1))


print power(3, 2)