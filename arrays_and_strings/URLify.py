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

import unittest

def urlify(string, length):
    """function replaces single spaces with %20 and removes trailing spaces"""
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string

class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
