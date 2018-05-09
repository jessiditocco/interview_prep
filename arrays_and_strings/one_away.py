def one_away(str1, str2):
    """Write a function to check if two strings are one edit (or zero) away
    >>> one_away("pale", "ple")
    True

    >>> one_away("pale", "pales")
    True

    >>> one_away("pales", "bales")
    True

    >>> one_away("pale", "bake")
    False

    >>> one_away("pale", "bale")
    True

    >>> one_away("paleabc", "pleabc")
    True

    >>> one_away("a", "b")
    True

    >>> one_away(" ", "d")
    True

    >>> one_away("pale", "pale")
    True

    >>> one_away("ple", "pale")
    True

    >>> one_away("pal", "palks")
    False
    """
    
    different = 0

    if str1 == str2:
        return True

    if abs(len(str1) - len(str2)) > 1:
        return False

    if (len(str1) - 1 == len(str2)) or (len(str2) - 1 == len(str1)):
        if len(str1) < len(str2):
            for char in str1:
                if char not in str2:
                    return False

        else:
            for char in str2:
                if char not in str1:
                    return False

    elif len(str1) == len(str2):
        for char in str1:
            if char not in str2:
                different += 1

                if different > 1:
                    return False
    return True


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed"