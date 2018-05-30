import unittest


def zero_matrix(matrix):
    """Replaces rows and columns of zero's with all zeros"""

    m = len(matrix)
    n = len(matrix[0])
    zero_rows = []
    zero_columns = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_rows.append(i)
                zero_columns.append(j)

    # now we have the indices of the zero columns and rows
    # saved in an array

    for row in zero_rows:
        nullify_row(matrix, row)

    for column in zero_columns:
        nullify_column(matrix, column)

    return matrix


def nullify_row(matrix, row):
    """Replaces zero rows with zeros"""

    for i in range(len(matrix[0])):
        matrix[row][i] = 0

def nullify_column(matrix, column):
    """Replaces all columns with zeros"""

    for i in range(len(matrix)):
        matrix[i][column] = 0




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()


# Runtime is O(MxN)


