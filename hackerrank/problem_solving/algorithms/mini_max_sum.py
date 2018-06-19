def min_max_values(numbers):
    increasing = sorted(numbers)
    decreasing = sorted(numbers, reverse=True)

    min_sum = 0
    max_sum = 0

    for i in range(4):
        min_sum += increasing[i]
        max_sum += decreasing[i]

    print min_sum, max_sum




if __name__ == "__main__":
    numbers = map(int, raw_input().split())

    min_max_values(numbers)