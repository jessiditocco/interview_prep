def count_consecutive_ones(base_10):

    binary = convert_to_binary(base_10)

    # print binary
    # print type(binary)

    consecutive = 0

    consecutive_ones = []

    for digit in binary:
        if int(digit) == 1:
            consecutive += 1
        else:
            consecutive_ones.append(consecutive)
            consecutive = 0

    consecutive_ones.append(consecutive)

    print max(consecutive_ones)
    return max(consecutive_ones)

def convert_to_binary(dividend):

    # import pdb; pdb.set_trace()

    if dividend <= 1:
        return "1"

    quotient = str(dividend // 2)
    remainder = str(dividend % 2)

    return convert_to_binary(int(quotient)) + remainder
    
# print convert_to_binary(0)
# print convert_to_binary(1)
# print convert_to_binary(2)
# print convert_to_binary(3)
# print convert_to_binary(4)
# print convert_to_binary(5)
# print convert_to_binary(7)


if __name__ == "__main__":
    base_10 = int(raw_input())

    count_consecutive_ones(base_10)