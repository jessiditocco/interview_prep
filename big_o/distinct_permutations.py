from math import factorial 
from collections import Counter

# we will define a function called distinct permutations that takes in a string
# we will use the Counter module to make a dictionary of the number of occurances for each letter
# we will return the factorial of the length of the string / factorial for each occurance that is
# greater than 1


def permutation_count(s):
    """Return the number of different permutations of s."""
    
    s = str(s)

    counter = Counter(s)

    c = 1

    for i in counter.values():
        c *= factorial(i)

    return factorial(len(s)) // c


print permutation_count('AAAABBBCCDDEEFFGHIJKLMNOPQRSTUVWXYZ')