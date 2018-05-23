def string_compression(str1):
    """
    >>> string_compression("abcdefg")
    'abcdefg'

    >>> string_compression("aabcccccaaa")
    'a2b1c5a3'

    >>> string_compression("aaabbccccccaaabb")
    'a3b2c6a3b2'

    >>> string_compression("aabbccdd")
    'aabbccdd'

    >>> string_compression("")
    ''

    """

    if str1 == "":
        return str1

    current = str1[0]
    count = 0
    compressed = []

    for char in str1:
        if current == char:
            count += 1
            # print "{} is equal to {}".format(current, char)

        else:
            # print "{} is not equal to {}".format(current, char)
            compressed.append(current)
            compressed.append(str(count))

            current = char
            count = 1

    # once we get to the end of the string iteration, we must append the final letter
    # and count
    compressed.append(current)
    compressed.append(str(count))

    # print compressed

    if len(compressed) < len(str1):
        return "".join(compressed)
    else:
        return str1



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!!"