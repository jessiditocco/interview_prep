def is_unique(str):
    """Checks whether a string has all unique charecters
    >>> is_unique("abc123")
    True

    >>> is_unique("abcc123")
    False
    """

    # char_count = {}

    # for char in str:
    #     count = char_count.get(char, 0)

    #     if count == 1:
    #         return False

    #     else:
    #         char_count[char] = 1

    # return True

    return len(str) == len(set(str))


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!"