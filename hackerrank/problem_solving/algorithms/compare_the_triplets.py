def compare_the_triplets(a, b):
    alice_comparison_points = 0
    bob_comparison_points = 0

    for i in range(3):
        if a[i] > b[i]:
            alice_comparison_points += 1
        elif a[i] < b[i]:
            bob_comparison_points += 1

    return "{} {}".format(alice_comparison_points, bob_comparison_points)


line1 = (5, 6, 7)
line2 = (3, 6, 10)

print compare_the_triplets(line1, line2)

