def is_permutation(str1, str2):
    """Given two strings, check wehther one is the permutation of the other.

    >>> is_permutation('hio', 'oih')
    True

    >>> is_permutation('HiO', 'oih')
    False

    >>> is_permutation('', '')
    True
    """

########## solution 1 #######################
    # if not str1 and not str2:
    #     return True

    # str1_count = {}
    # str2_count = {}

    # for char in str1:
    #     str1_count[char] = str1_count.get(char, 0) + 1

    # for char in str2:
    #     str2_count[char] = str2_count.get(char, 0) + 1

    # if str1_count == str2_count:
    #     return True

    # return False

########## solution 2-- Not as efficient but good readability #######################


    # sorted1 = sorted(str1)
    # sorted2 = sorted(str2)

    # if sorted1 == sorted2:
    #     return True
    # return False

########## solution 3 #######################

    
    counter = {}

    for char in str1:
        counter[char] = counter.get(char, 0) + 1

    for char in str2:
        if char not in counter: 
            return False
        counter[char] -= 1

        if counter[char] == 0:
            del counter[char]

    return len(counter) == 0



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All doctests passed!"