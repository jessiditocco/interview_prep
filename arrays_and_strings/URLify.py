# def urlify(s):
#     """Replaces all of the spaces in a string with %20

#     >>> urlify('hi my name is')
#     'hi%20my%20name%20is'

#     >>> urlify('hi my name is     ')
#     'hi%20my%20name%20is'

#     >>> urlify('')
#     ''
#     """

#     # without_whitespace = s.strip()

#     # split = without_whitespace.split(" ")

#     # return "%20".join(split)


# if __name__ == "__main__":
#     import doctest
#     if doctest.testmod().failed == 0:
#         print "All doctests passed!! Wooo"


def urlify(s, true_length):
    """Replaces all of the spaces in a string with %20

    >>> urlify('hi my name is', 13)
    hi%20my%20name%20is

    >>> urlify('hi my name is     ', 13)
    hi%20my%20name%20is

    """


    string_list = list(s)

    for i in reversed(range(true_length)):
        if string_list[i] == " ":
            string_list[i] = "%20"

    print "".join(string_list)


urlify('hi my name is', 13)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All doctests passed!! Wooo"

