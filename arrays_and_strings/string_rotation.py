import unittest

def is_rotation(s1, s2):
    """Checks that two strings are rotations of one another"""

    # check that the lengths of the strings are equal and greater than zero

    if len(s1) == len(s2) != 0:
        return is_a_substring(s1 + s1, s2)
    else:
        return False

def is_a_substring(concatenated_string, sub):

    if concatenated_string.find(sub) != -1:
        return True

    else:
        return False


class Test(unittest.TestCase):
    data = [("waterbottle", "erbottlewat", True), 
    ("hotdog", "tdogho", True), ("foo", "foofoo", False), 
    ("foo", "bar", False)]

    def test_string_rotatation(self):
        for [s1, s2, expected] in self.data:
            actual = is_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
