def sum_digits_in_num(n):

    # n = 153
    sum_digits = 0

    while n > 0:
        num_to_add = n % 10
        sum_digits += num_to_add
        n = n / 10

    return sum_digits


print sum_digits_in_num(1535)