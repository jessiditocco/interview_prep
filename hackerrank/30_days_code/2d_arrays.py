def max_hourglass_sum(arr):
    rows = len(arr)
    cols = len(arr[0])

    hourglass_sums = []

    for i in range((cols / 2) + 1):
        for j in range((rows / 2) + 1):

            sum_houglass = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + 
                            arr[i + 1][j + 1] +
                            arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])

            hourglass_sums.append(sum_houglass)

    print max(hourglass_sums)



if __name__ == "__main__":
    
    two_dimensional_array = []

    for i in range(6):
        line = map(int, raw_input().rstrip().split())
        two_dimensional_array.append(line)

    max_hourglass_sum(two_dimensional_array)
