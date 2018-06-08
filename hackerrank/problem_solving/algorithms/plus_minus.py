def plus_minus(arr, n):

    positive = 0
    negative = 0
    zero = 0

    for i in range(n):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zero += 1

    print float(positive) / n
    print float(negative) / n
    print float(zero) / n


if __name__ == "__main__":
    arr = [-4, 3, -9, 0, 4, 1]
    plus_minus(arr, 6)