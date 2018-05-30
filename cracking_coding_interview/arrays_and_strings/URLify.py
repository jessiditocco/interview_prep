def urlify(s):
    """Replaces all of the spaces in a string with %20

    >>> urlify('hi my name is')
    'hi%20my%20name%20is'

    >>> urlify('hi my name is     ')
    'hi%20my%20name%20is'

    >>> urlify('')
    ''
    """

    without_whitespace = s.strip()

    split = without_whitespace.split(" ")

    return "%20".join(split)


# if __name__ == "__main__":
#     import doctest
#     if doctest.testmod().failed == 0:
#         print "All doctests passed!! Wooo"


# def urlify(str, true_length):
#     """Replaces all of the spaces in a string with %20

#     >>> urlify('hi my name is', 13)
#     hi%20my%20name%20is

#     >>> urlify('hi my name is     ', 13)
#     hi%20my%20name%20is

#     """

#     # Listify the string --> each charecter will be its own index
#     char_list = list(str)
#     # Keep track of the new index which will be the length of the list
#     new_index = len(char_list)
#     # Loop through the indices from the reversed range of true_length
#     # If the charecter is a space, replace the space with the "%20"
#     # If the charecter is a letter/number, move the letter one index back

#     print char_list
#     print new_index

#     for i in reversed(range(true_length)):
#         if char_list[i] == " ":
#             char_list[new_index - 3: new_index] = "%20"
#             new_index -= 3

#         else:
#             char_list[new_index - 1] = char_list[i]
#             new_index -= 1

#     return " ".join(char_list)


# print urlify('hi dog hi    ', 9)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All doctests passed!! Wooo"

