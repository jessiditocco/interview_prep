def reverse_array(a):

    reversed_array = []

    for i in a[::-1]:
        reversed_array.append(str(i))

    return " ".join(reversed_array)


print reverse_array([1, 2, 3, 4])