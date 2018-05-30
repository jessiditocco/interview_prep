import unittest

# Watson gives Sherlock an array of integers. 
# His challenge is to find an element of the array such that the sum of all 
# elements to the left is equal to the sum of all elements to the right. 
# For instance, given the array [5,6,8,11], 8  is between two subarray that sum to 11. 
# If your starting array is [1], that element satisfies the rule as left and 
# right sum to 0.

# You will be given arrays of integers and must determine whether there is 
# an element that meets the criterion.


# [5,6,8,11], 8

def sherlock_and_array(a):
    # set left index equal to 0
    # set right index equal to length of the array minus 1
    # set left sum equal to the array at the first index
    # set the right sum equal to the array at the last index

    # while left index is less than the right index
    # if the left sum is greater than the right sum, decrement the right index, increment right sum
    # if the right sum is greater than the left sum, increment the left index, increment the left sum

    # once broken out of the loop, check to see of the right and left sum are equal

    left_index = 0
    right_index = len(a) - 1

    left_sum = a[left_index]
    right_sum = a[right_index]

    while left_index != right_index:
        if left_sum > right_sum:
            right_index -= 1
            right_sum += a[right_index]
        else:
            left_index += 1
            left_sum += a[left_index]

    if right_sum == left_sum:
        return True

    else:
        return False

class Test(unittest.TestCase):
    """Tests sherlock and array"""

    data = [([5,6,8,11], True), 
            ([2], True), 
            ([5,6,7,7], False)]

    def test_sherlock_array(self):
        for test, expected in self.data:
            actual = sherlock_and_array(test)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()


# print sherlock_and_array([5,6,8,11])
# print sherlock_and_array([1])