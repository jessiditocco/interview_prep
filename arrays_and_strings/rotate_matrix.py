def rotate_matrix(matrix):
    """Rotates a matrix 90 degrees clockwise"""

    length_matrix = len(matrix)

    for layer in range(length_matrix//2):

        first = layer
        last = length_matrix - layer - 1

        for i in range(first, last):
            # save the top value
            top = matrix[layer][i]

            # move bottom left to top
            matrix[layer][i] = matrix[-i - 1][layer]

            # move the botom right to the bottom left
            matrix[-i - 1][layer] = matrix[-layer -1][-i - 1]

            # move the top right to bottom left
            matrix[-layer -1][-i - 1] = matrix[i][- layer - 1]

            # replace the top to the right 
            matrix[i][- layer - 1] = top

    return matrix

print rotate_matrix([["a","b","c"],
          [1,2,3],
          ["x","y","z"]])



# https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/7_Rotate%20Matrix/RotateMatrix.py