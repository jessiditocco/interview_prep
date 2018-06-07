def largest_hourglass_sum(arr, lines):

    sums = []
    
    for i in range((lines / 2) + 1):
        for j in range((lines / 2) + 1):
            hourglass_sum = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])

            sums.append(hourglass_sum)
            
    print max(sums)
    return max(sums)

# print arr[i][j]
# print arr[i][j + 1]
# print arr[i][j + 2]

# print arr[i+1][j+1]

# print arr[i+2][j]
# print arr[i+2][j+1]
# print arr[i+2][j+2]



# print arr[0][0], arr[0][1], arr[0][2]
# print " ", arr[1][1]
# print arr[2][0], arr[2][1], arr[2][2]


if __name__ == "__main__":
    arr = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]
            ]

    arr2 = [
            [-9, -9, -9,  1, 1, 1],
            [0, -9, 0, 4, 3, 2], 
            [-9, -9, -9, 1, 2, 3], 
            [0, 0, 8, 6, 6, 0], 
            [0, 0, 0, -2, 0, 0], 
            [0, 0, 1, 2, 4, 0]
            ]


    largest_hourglass_sum(arr, 6)
    largest_hourglass_sum(arr2, 6)