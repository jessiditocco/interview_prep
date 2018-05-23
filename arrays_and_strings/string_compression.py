def string_compression(str1):
    """
    >>> string_compression("abcdefg")
    'abcdefg'

    >>> string_compression("aabbbcdddeefg")
    'a2b3c1d3e2f1g1'
    """

    str1_chars = set(str1)
    if len(str1) == len(str1_chars):
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

    return "".join(compressed)


# print string_compression("aabbbcdddeefg")


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!!"